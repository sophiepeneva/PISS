# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Bus.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Bus.proto',
  package='bus',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\tBus.proto\x12\x03\x62us\"(\n\nBusRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0e\n\x06number\x18\x02 \x01(\x05\"`\n\x0b\x42usResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0e\n\x06number\x18\x02 \x01(\x05\x12\x17\n\x0fpeople_capacity\x18\x03 \x01(\x05\x12\x1c\n\x14\x61verage_people_count\x18\x04 \x01(\x02\x32\x44\n\x08\x44yonysus\x12\x38\n\x11GetServerResponse\x12\x0f.bus.BusRequest\x1a\x10.bus.BusResponse\"\x00\x62\x06proto3'
)




_BUSREQUEST = _descriptor.Descriptor(
  name='BusRequest',
  full_name='bus.BusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bus.BusRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='number', full_name='bus.BusRequest.number', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=58,
)


_BUSRESPONSE = _descriptor.Descriptor(
  name='BusResponse',
  full_name='bus.BusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='bus.BusResponse.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='number', full_name='bus.BusResponse.number', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='people_capacity', full_name='bus.BusResponse.people_capacity', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='average_people_count', full_name='bus.BusResponse.average_people_count', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=156,
)

DESCRIPTOR.message_types_by_name['BusRequest'] = _BUSREQUEST
DESCRIPTOR.message_types_by_name['BusResponse'] = _BUSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BusRequest = _reflection.GeneratedProtocolMessageType('BusRequest', (_message.Message,), {
  'DESCRIPTOR' : _BUSREQUEST,
  '__module__' : 'Bus_pb2'
  # @@protoc_insertion_point(class_scope:bus.BusRequest)
  })
_sym_db.RegisterMessage(BusRequest)

BusResponse = _reflection.GeneratedProtocolMessageType('BusResponse', (_message.Message,), {
  'DESCRIPTOR' : _BUSRESPONSE,
  '__module__' : 'Bus_pb2'
  # @@protoc_insertion_point(class_scope:bus.BusResponse)
  })
_sym_db.RegisterMessage(BusResponse)



_DYONYSUS = _descriptor.ServiceDescriptor(
  name='Dyonysus',
  full_name='bus.Dyonysus',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=158,
  serialized_end=226,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetServerResponse',
    full_name='bus.Dyonysus.GetServerResponse',
    index=0,
    containing_service=None,
    input_type=_BUSREQUEST,
    output_type=_BUSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DYONYSUS)

DESCRIPTOR.services_by_name['Dyonysus'] = _DYONYSUS

# @@protoc_insertion_point(module_scope)