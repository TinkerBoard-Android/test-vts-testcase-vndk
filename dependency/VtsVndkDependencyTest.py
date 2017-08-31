#!/usr/bin/env python
#
# Copyright (C) 2017 The Android Open Source Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import logging
import os
import re
import shutil
import tempfile

from vts.runners.host import asserts
from vts.runners.host import base_test
from vts.runners.host import test_runner
from vts.runners.host import utils
from vts.testcases.vndk.golden import vndk_data
from vts.utils.python.controllers import android_device
from vts.utils.python.file import target_file_utils
from vts.utils.python.library import elf_parser
from vts.utils.python.os import path_utils


class VtsVndkDependencyTest(base_test.BaseTestClass):
    """A test case to verify vendor library dependency.

    Attributes:
        _dut: The AndroidDevice under test.
        _temp_dir: The temporary directory to which the vendor partition is
                   copied.
        _ll_ndk: Set of strings. The names of low-level NDK libraries in
                 /system/lib[64].
        _sp_ndk: Set of strings. The names of same-process NDK libraries in
                 /system/lib[64]/vndk.
        _vndk_sp: Set of strings. The names of VNDK-SP libraries in
                  /system/lib[64]/vndk-sp.
        _SAME_PROCESS_HAL: List of patterns. The names of same-process HAL
                           libraries expected to be in /vendor/lib[64].
    """
    _TARGET_VENDOR_DIR = "/vendor"

    # copied from development/vndk/tools/definition-tool/vndk_definition_tool.py
    _SAME_PROCESS_HAL = [
        re.compile(p)
        for p in [
            "android\\.hardware\\.graphics\\.mapper@\\d+\\.\\d+-impl\\.so$",
            "gralloc\\..*\\.so$", "libEGL_.*\\.so$", "libGLES_.*\\.so$",
            "libGLESv1_CM_.*\\.so$", "libGLESv2_.*\\.so$",
            "libGLESv3_.*\\.so$", "libPVRRS\\.so$", "libRSDriver.*\\.so$",
            "vulkan.*\\.so$"
        ]
    ]
    _SP_HAL_LINK_PATHS_32 = [
        "/vendor/lib/egl", "/vendor/lib/hw", "/vendor/lib"
    ]
    _SP_HAL_LINK_PATHS_64 = [
        "/vendor/lib64/egl", "/vendor/lib64/hw", "/vendor/lib64"
    ]

    class ElfObject(object):
        """Contains dependencies of an ELF file on target device.

        Attributes:
            target_path: String. The path to the ELF file on target.
            name: String. File name of the ELF.
            target_dir: String. The directory containing the ELF file on target.
            bitness: Integer. Bitness of the ELF.
            deps: List of strings. The names of the depended libraries.
        """

        def __init__(self, target_path, bitness, deps):
            self.target_path = target_path
            self.name = path_utils.TargetBaseName(target_path)
            self.target_dir = path_utils.TargetDirName(target_path)
            self.bitness = bitness
            self.deps = deps

    def setUpClass(self):
        """Initializes device, temporary directory, and VNDK lists."""
        self._dut = self.android_devices[0]
        self._temp_dir = tempfile.mkdtemp()
        logging.info("adb pull %s %s", self._TARGET_VENDOR_DIR, self._temp_dir)
        pull_output = self._dut.adb.pull(self._TARGET_VENDOR_DIR,
                                         self._temp_dir)
        logging.debug(pull_output)
        vndk_lists = vndk_data.LoadVndkLibraryLists(
            "current", vndk_data.LL_NDK, vndk_data.SP_NDK, vndk_data.VNDK_SP)
        asserts.assertTrue(vndk_lists, "Cannot load VNDK library lists.")
        self._ll_ndk, self._sp_ndk, self._vndk_sp = (
            set(path_utils.TargetBaseName(path) for path in vndk_list)
            for vndk_list in vndk_lists)
        logging.debug("LL_NDK: %s", self._ll_ndk)
        logging.debug("SP_NDK: %s", self._sp_ndk)
        logging.debug("VNDK_SP: %s", self._vndk_sp)

    def tearDownClass(self):
        """Deletes the temporary directory."""
        logging.info("Delete %s", self._temp_dir)
        shutil.rmtree(self._temp_dir)

    def _LoadElfObjects(self, host_dir, target_dir, elf_error_handler):
        """Scans a host directory recursively and loads all ELF files in it.

        Args:
            host_dir: The host directory to scan.
            target_dir: The path from which host_dir is copied.
            elf_error_handler: A function that takes 2 arguments
                               (target_path, exception). It is called when
                               the parser fails to read an ELF file.

        Returns:
            List of ElfObject.
        """
        objs = []
        for root_dir, file_name in utils.iterate_files(host_dir):
            full_path = os.path.join(root_dir, file_name)
            rel_path = os.path.relpath(full_path, host_dir)
            target_path = path_utils.JoinTargetPath(
                target_dir, *rel_path.split(os.path.sep))
            try:
                elf = elf_parser.ElfParser(full_path)
            except elf_parser.ElfError:
                logging.debug("%s is not an ELF file", target_path)
                continue
            try:
                deps = elf.ListDependencies()
            except elf_parser.ElfError as e:
                elf_error_handler(target_path, e)
                continue
            finally:
                elf.Close()

            logging.info("%s depends on: %s", target_path, ", ".join(deps))
            objs.append(self.ElfObject(target_path, elf.bitness, deps))
        return objs

    def _IsAllowedSpHalDependency(self, lib_name, linkable_libs):
        """Checks whether a same-process HAL library dependency is allowed.

        A same-process HAL library is allowed to depend on
        - Low-level NDK
        - Same-process NDK
        - vndk-sp
        - Other libraries in vendor/lib[64]

        Args:
            lib_name: String. The name of the depended library.
            linkable_libs: Dictionary. The keys are the names of the libraries
                           which can be linked to same-process HAL.

        Returns:
            A boolean representing whether the dependency is allowed.
        """
        if (lib_name in self._ll_ndk or
            lib_name in self._sp_ndk or
            lib_name in self._vndk_sp or
            lib_name in linkable_libs):
            return True
        return False

    def _GetSpHalLinkPaths(self, bitness):
        """Returns 32/64-bit same-process HAL link paths"""
        return getattr(self, "_SP_HAL_LINK_PATHS_" + str(bitness))

    def _IsInSpHalLinkPaths(self, lib):
        """Checks whether a library can be linked to same-process HAL.

        Args:
            lib: ElfObject. The library to check.

        Returns:
            True if can be linked to same-process HAL; False otherwise.
        """
        return lib.target_dir in self._GetSpHalLinkPaths(lib.bitness)

    def _SpHalLinkOrder(self, lib):
        """Returns the key for sorting libraries in linker search order.

        Args:
            lib: ElfObject.

        Returns:
            An integer representing linker search order.
        """
        link_paths = self._GetSpHalLinkPaths(lib.bitness)
        for order in range(len(link_paths)):
            if lib.target_dir == link_paths[order]:
                return order
        order = len(link_paths)
        if lib.name in self._ll_ndk:
            return order
        order += 1
        if lib.name in self._sp_ndk:
            return order
        order += 1
        return order

    def _DfsDependencies(self, lib, searched, searchable):
        """Depth-first-search for library dependencies.

        Args:
            lib: ElfObject. The library to search dependencies.
            searched: The set of searched libraries.
            searchable: The dictionary that maps file names to libraries.
        """
        if lib in searched:
            return
        searched.add(lib)
        for dep_name in lib.deps:
            if dep_name in searchable:
                self._DfsDependencies(searchable[dep_name], searched,
                                      searchable)

    def _TestSpHalDependency(self, bitness, objs):
        """Scans same-process HAL dependency on vendor partition.

        Returns:
            List of tuples (path, dependency_names). The library with
            disallowed dependencies and list of the dependencies.
        """
        # map file names to libraries which can be linked to same-process HAL
        linkable_libs = dict()
        for obj in [
                x for x in objs
                if x.bitness == bitness and self._IsInSpHalLinkPaths(x)
        ]:
            if obj.name not in linkable_libs:
                linkable_libs[obj.name] = obj
            else:
                linkable_libs[obj.name] = min(
                    linkable_libs[obj.name], obj, key=self._SpHalLinkOrder)
        # find same-process HAL and dependencies
        sp_hal_libs = set()
        for file_name, obj in linkable_libs.iteritems():
            if any([x.match(file_name) for x in self._SAME_PROCESS_HAL]):
                self._DfsDependencies(obj, sp_hal_libs, linkable_libs)
        logging.info("%d-bit SP HAL libraries: %s" %
                     (bitness, ", ".join([x.name for x in sp_hal_libs])))
        # check disallowed dependencies
        dep_errors = []
        for obj in sp_hal_libs:
            disallowed_libs = [
                x for x in obj.deps
                if not self._IsAllowedSpHalDependency(x, linkable_libs)
            ]
            if disallowed_libs:
                dep_errors.append((obj.target_path, disallowed_libs))
        return dep_errors

    def testElfDependency(self):
        """Scans library/executable dependency on vendor partition."""
        read_errors = []
        objs = self._LoadElfObjects(
            self._temp_dir,
            path_utils.TargetDirName(self._TARGET_VENDOR_DIR),
            lambda p, e: read_errors.append((p, str(e))))

        dep_errors = self._TestSpHalDependency(32, objs)
        if self._dut.is64Bit:
            dep_errors.extend(self._TestSpHalDependency(64, objs))
        # TODO(hsinyichen): check other vendor libraries

        if read_errors:
            logging.error("%d read errors:", len(read_errors))
            for x in read_errors:
                logging.error("%s: %s", x[0], x[1])
        if dep_errors:
            logging.error("%d disallowed dependencies:", len(dep_errors))
            for x in dep_errors:
                logging.error("%s: %s", x[0], ", ".join(x[1]))
        error_count = len(read_errors) + len(dep_errors)
        asserts.assertEqual(error_count, 0,
                            "Total number of errors: " + str(error_count))


if __name__ == "__main__":
    test_runner.main()
