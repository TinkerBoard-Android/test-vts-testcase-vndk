# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: VndkAbiDump.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='VndkAbiDump.proto',
  package='android.vts',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x11VndkAbiDump.proto\x12\x0b\x61ndroid.vts\"\xac\x02\n\x0bVTableEntry\x12\x0e\n\x06offset\x18\x01 \x01(\x03\x12\x36\n\x04kind\x18\x02 \x01(\x0e\x32\x1d.android.vts.VTableEntry.Kind:\tUNDEFINED\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x16\n\x0e\x64\x65mangled_name\x18\x04 \x01(\t\x12\x16\n\x07is_pure\x18\x05 \x01(\x08:\x05\x66\x61lse\"\x96\x01\n\x04Kind\x12\r\n\tUNDEFINED\x10\x00\x12\x0f\n\x0bVCALLOFFSET\x10\x01\x12\x0f\n\x0bVBASEOFFSET\x10\x02\x12\x0f\n\x0bOFFSETTOTOP\x10\x03\x12\x08\n\x04RTTI\x10\x04\x12\x10\n\x0cVFUNCPOINTER\x10\x05\x12\x17\n\x13\x44\x45LETINGDTORPOINTER\x10\x06\x12\x17\n\x13\x43OMPLETEDTORPOINTER\x10\x07\"`\n\x06VTable\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x16\n\x0e\x64\x65mangled_name\x18\x02 \x01(\t\x12\x30\n\x0evtable_entries\x18\x03 \x03(\x0b\x32\x18.android.vts.VTableEntry\"\x91\x01\n\x06Symbol\x12@\n\x07\x62inding\x18\x01 \x01(\x0e\x32$.android.vts.Symbol.ElfSymbolBinding:\tUNDEFINED\x12\x0c\n\x04name\x18\x02 \x01(\t\"7\n\x10\x45lfSymbolBinding\x12\r\n\tUNDEFINED\x10\x00\x12\n\n\x06GLOBAL\x10\x01\x12\x08\n\x04WEAK\x10\x02\"U\n\x07\x41\x62iDump\x12$\n\x07vtables\x18\x01 \x03(\x0b\x32\x13.android.vts.VTable\x12$\n\x07symbols\x18\x02 \x03(\x0b\x32\x13.android.vts.Symbol')
)



_VTABLEENTRY_KIND = _descriptor.EnumDescriptor(
  name='Kind',
  full_name='android.vts.VTableEntry.Kind',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VCALLOFFSET', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VBASEOFFSET', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OFFSETTOTOP', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RTTI', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VFUNCPOINTER', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETINGDTORPOINTER', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPLETEDTORPOINTER', index=7, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=185,
  serialized_end=335,
)
_sym_db.RegisterEnumDescriptor(_VTABLEENTRY_KIND)

_SYMBOL_ELFSYMBOLBINDING = _descriptor.EnumDescriptor(
  name='ElfSymbolBinding',
  full_name='android.vts.Symbol.ElfSymbolBinding',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GLOBAL', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WEAK', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=526,
  serialized_end=581,
)
_sym_db.RegisterEnumDescriptor(_SYMBOL_ELFSYMBOLBINDING)


_VTABLEENTRY = _descriptor.Descriptor(
  name='VTableEntry',
  full_name='android.vts.VTableEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='offset', full_name='android.vts.VTableEntry.offset', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kind', full_name='android.vts.VTableEntry.kind', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='android.vts.VTableEntry.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='demangled_name', full_name='android.vts.VTableEntry.demangled_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_pure', full_name='android.vts.VTableEntry.is_pure', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _VTABLEENTRY_KIND,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=335,
)


_VTABLE = _descriptor.Descriptor(
  name='VTable',
  full_name='android.vts.VTable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='android.vts.VTable.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='demangled_name', full_name='android.vts.VTable.demangled_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vtable_entries', full_name='android.vts.VTable.vtable_entries', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=337,
  serialized_end=433,
)


_SYMBOL = _descriptor.Descriptor(
  name='Symbol',
  full_name='android.vts.Symbol',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='binding', full_name='android.vts.Symbol.binding', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='android.vts.Symbol.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SYMBOL_ELFSYMBOLBINDING,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=436,
  serialized_end=581,
)


_ABIDUMP = _descriptor.Descriptor(
  name='AbiDump',
  full_name='android.vts.AbiDump',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vtables', full_name='android.vts.AbiDump.vtables', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='symbols', full_name='android.vts.AbiDump.symbols', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=583,
  serialized_end=668,
)

_VTABLEENTRY.fields_by_name['kind'].enum_type = _VTABLEENTRY_KIND
_VTABLEENTRY_KIND.containing_type = _VTABLEENTRY
_VTABLE.fields_by_name['vtable_entries'].message_type = _VTABLEENTRY
_SYMBOL.fields_by_name['binding'].enum_type = _SYMBOL_ELFSYMBOLBINDING
_SYMBOL_ELFSYMBOLBINDING.containing_type = _SYMBOL
_ABIDUMP.fields_by_name['vtables'].message_type = _VTABLE
_ABIDUMP.fields_by_name['symbols'].message_type = _SYMBOL
DESCRIPTOR.message_types_by_name['VTableEntry'] = _VTABLEENTRY
DESCRIPTOR.message_types_by_name['VTable'] = _VTABLE
DESCRIPTOR.message_types_by_name['Symbol'] = _SYMBOL
DESCRIPTOR.message_types_by_name['AbiDump'] = _ABIDUMP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VTableEntry = _reflection.GeneratedProtocolMessageType('VTableEntry', (_message.Message,), dict(
  DESCRIPTOR = _VTABLEENTRY,
  __module__ = 'VndkAbiDump_pb2'
  # @@protoc_insertion_point(class_scope:android.vts.VTableEntry)
  ))
_sym_db.RegisterMessage(VTableEntry)

VTable = _reflection.GeneratedProtocolMessageType('VTable', (_message.Message,), dict(
  DESCRIPTOR = _VTABLE,
  __module__ = 'VndkAbiDump_pb2'
  # @@protoc_insertion_point(class_scope:android.vts.VTable)
  ))
_sym_db.RegisterMessage(VTable)

Symbol = _reflection.GeneratedProtocolMessageType('Symbol', (_message.Message,), dict(
  DESCRIPTOR = _SYMBOL,
  __module__ = 'VndkAbiDump_pb2'
  # @@protoc_insertion_point(class_scope:android.vts.Symbol)
  ))
_sym_db.RegisterMessage(Symbol)

AbiDump = _reflection.GeneratedProtocolMessageType('AbiDump', (_message.Message,), dict(
  DESCRIPTOR = _ABIDUMP,
  __module__ = 'VndkAbiDump_pb2'
  # @@protoc_insertion_point(class_scope:android.vts.AbiDump)
  ))
_sym_db.RegisterMessage(AbiDump)


# @@protoc_insertion_point(module_scope)