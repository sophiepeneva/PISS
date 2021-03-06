# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: apollo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='apollo.proto',
  package='gen',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0c\x61pollo.proto\x12\x03gen\"\x1f\n\x11\x42usDetailsRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"\xb3\x01\n\x12\x42usDetailsResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0e\n\x06number\x18\x02 \x01(\x05\x12 \n\x18standing_people_capacity\x18\x03 \x01(\x05\x12\x1f\n\x17sitting_people_capacity\x18\x04 \x01(\x05\x12 \n\x18\x64isabled_people_capacity\x18\x05 \x01(\x05\x12\x1c\n\x14\x61verage_people_count\x18\x06 \x01(\x02\x32L\n\x06\x41pollo\x12\x42\n\rGetBusDetails\x12\x16.gen.BusDetailsRequest\x1a\x17.gen.BusDetailsResponse\"\x00\x62\x06proto3'
)




_BUSDETAILSREQUEST = _descriptor.Descriptor(
  name='BusDetailsRequest',
  full_name='gen.BusDetailsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='gen.BusDetailsRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=21,
  serialized_end=52,
)


_BUSDETAILSRESPONSE = _descriptor.Descriptor(
  name='BusDetailsResponse',
  full_name='gen.BusDetailsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='gen.BusDetailsResponse.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='number', full_name='gen.BusDetailsResponse.number', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='standing_people_capacity', full_name='gen.BusDetailsResponse.standing_people_capacity', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sitting_people_capacity', full_name='gen.BusDetailsResponse.sitting_people_capacity', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='disabled_people_capacity', full_name='gen.BusDetailsResponse.disabled_people_capacity', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='average_people_count', full_name='gen.BusDetailsResponse.average_people_count', index=5,
      number=6, type=2, cpp_type=6, label=1,
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
  serialized_start=55,
  serialized_end=234,
)

DESCRIPTOR.message_types_by_name['BusDetailsRequest'] = _BUSDETAILSREQUEST
DESCRIPTOR.message_types_by_name['BusDetailsResponse'] = _BUSDETAILSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BusDetailsRequest = _reflection.GeneratedProtocolMessageType('BusDetailsRequest', (_message.Message,), {
  'DESCRIPTOR' : _BUSDETAILSREQUEST,
  '__module__' : 'apollo_pb2'
  # @@protoc_insertion_point(class_scope:gen.BusDetailsRequest)
  })
_sym_db.RegisterMessage(BusDetailsRequest)

BusDetailsResponse = _reflection.GeneratedProtocolMessageType('BusDetailsResponse', (_message.Message,), {
  'DESCRIPTOR' : _BUSDETAILSRESPONSE,
  '__module__' : 'apollo_pb2'
  # @@protoc_insertion_point(class_scope:gen.BusDetailsResponse)
  })
_sym_db.RegisterMessage(BusDetailsResponse)



_APOLLO = _descriptor.ServiceDescriptor(
  name='Apollo',
  full_name='gen.Apollo',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=236,
  serialized_end=312,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetBusDetails',
    full_name='gen.Apollo.GetBusDetails',
    index=0,
    containing_service=None,
    input_type=_BUSDETAILSREQUEST,
    output_type=_BUSDETAILSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_APOLLO)

DESCRIPTOR.services_by_name['Apollo'] = _APOLLO

# @@protoc_insertion_point(module_scope)
