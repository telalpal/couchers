# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pb/api.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pb/api.proto',
  package='api',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0cpb/api.proto\x12\x03\x61pi\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\t\n\x07PingReq\"X\n\x07PingRes\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x1c\n\x14unread_message_count\x18\x04 \x01(\x03\"\xfa\x02\n\x04User\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04\x63ity\x18\x03 \x01(\t\x12\x14\n\x0cverification\x18\x04 \x01(\x01\x12\x1a\n\x12\x63ommunity_standing\x18\x05 \x01(\x01\x12\x16\n\x0enum_references\x18\x06 \x01(\r\x12\x0e\n\x06gender\x18\x07 \x01(\t\x12\x0b\n\x03\x61ge\x18\x08 \x01(\r\x12*\n\x06joined\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0blast_active\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\noccupation\x18\x0b \x01(\t\x12\x10\n\x08\x61\x62out_me\x18\x0c \x01(\t\x12\x13\n\x0b\x61\x62out_place\x18\r \x01(\t\x12\x11\n\tlanguages\x18\x0e \x03(\t\x12\x19\n\x11\x63ountries_visited\x18\x0f \x03(\t\x12\x17\n\x0f\x63ountries_lived\x18\x10 \x03(\t\"\x1a\n\nGetUserReq\x12\x0c\n\x04user\x18\x01 \x01(\t\"\xab\x04\n\x10UpdateProfileReq\x12*\n\x04name\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12*\n\x04\x63ity\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12,\n\x06gender\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x30\n\noccupation\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x08\x61\x62out_me\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0b\x61\x62out_place\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12<\n\tlanguages\x18\x07 \x01(\x0b\x32).api.UpdateProfileReq.RepeatedStringValue\x12\x44\n\x11\x63ountries_visited\x18\x08 \x01(\x0b\x32).api.UpdateProfileReq.RepeatedStringValue\x12\x42\n\x0f\x63ountries_lived\x18\t \x01(\x0b\x32).api.UpdateProfileReq.RepeatedStringValue\x1a\x34\n\x13RepeatedStringValue\x12\x0e\n\x06\x65xists\x18\x01 \x01(\x08\x12\r\n\x05value\x18\x02 \x03(\t\"\x88\x02\n\x10UpdateProfileRes\x12\x14\n\x0cupdated_name\x18\x01 \x01(\x08\x12\x14\n\x0cupdated_city\x18\x02 \x01(\x08\x12\x16\n\x0eupdated_gender\x18\x03 \x01(\x08\x12\x1a\n\x12updated_occupation\x18\x04 \x01(\x08\x12\x18\n\x10updated_about_me\x18\x05 \x01(\x08\x12\x1b\n\x13updated_about_place\x18\x06 \x01(\x08\x12\x19\n\x11updated_languages\x18\x07 \x01(\x08\x12!\n\x19updated_countries_visited\x18\x08 \x01(\x08\x12\x1f\n\x17updated_countries_lived\x18\t \x01(\x08\x32\x95\x01\n\x03\x41PI\x12$\n\x04Ping\x12\x0c.api.PingReq\x1a\x0c.api.PingRes\"\x00\x12\'\n\x07GetUser\x12\x0f.api.GetUserReq\x1a\t.api.User\"\x00\x12?\n\rUpdateProfile\x12\x15.api.UpdateProfileReq\x1a\x15.api.UpdateProfileRes\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_PINGREQ = _descriptor.Descriptor(
  name='PingReq',
  full_name='api.PingReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=86,
  serialized_end=95,
)


_PINGRES = _descriptor.Descriptor(
  name='PingRes',
  full_name='api.PingRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='api.PingRes.user_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='username', full_name='api.PingRes.username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='api.PingRes.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unread_message_count', full_name='api.PingRes.unread_message_count', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=97,
  serialized_end=185,
)


_USER = _descriptor.Descriptor(
  name='User',
  full_name='api.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='api.User.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='api.User.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='city', full_name='api.User.city', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='verification', full_name='api.User.verification', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='community_standing', full_name='api.User.community_standing', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_references', full_name='api.User.num_references', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gender', full_name='api.User.gender', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='age', full_name='api.User.age', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='joined', full_name='api.User.joined', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_active', full_name='api.User.last_active', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='occupation', full_name='api.User.occupation', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='about_me', full_name='api.User.about_me', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='about_place', full_name='api.User.about_place', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='languages', full_name='api.User.languages', index=13,
      number=14, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='countries_visited', full_name='api.User.countries_visited', index=14,
      number=15, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='countries_lived', full_name='api.User.countries_lived', index=15,
      number=16, type=9, cpp_type=9, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=188,
  serialized_end=566,
)


_GETUSERREQ = _descriptor.Descriptor(
  name='GetUserReq',
  full_name='api.GetUserReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='api.GetUserReq.user', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=568,
  serialized_end=594,
)


_UPDATEPROFILEREQ_REPEATEDSTRINGVALUE = _descriptor.Descriptor(
  name='RepeatedStringValue',
  full_name='api.UpdateProfileReq.RepeatedStringValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='exists', full_name='api.UpdateProfileReq.RepeatedStringValue.exists', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='api.UpdateProfileReq.RepeatedStringValue.value', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1100,
  serialized_end=1152,
)

_UPDATEPROFILEREQ = _descriptor.Descriptor(
  name='UpdateProfileReq',
  full_name='api.UpdateProfileReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='api.UpdateProfileReq.name', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='city', full_name='api.UpdateProfileReq.city', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gender', full_name='api.UpdateProfileReq.gender', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='occupation', full_name='api.UpdateProfileReq.occupation', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='about_me', full_name='api.UpdateProfileReq.about_me', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='about_place', full_name='api.UpdateProfileReq.about_place', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='languages', full_name='api.UpdateProfileReq.languages', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='countries_visited', full_name='api.UpdateProfileReq.countries_visited', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='countries_lived', full_name='api.UpdateProfileReq.countries_lived', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_UPDATEPROFILEREQ_REPEATEDSTRINGVALUE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=597,
  serialized_end=1152,
)


_UPDATEPROFILERES = _descriptor.Descriptor(
  name='UpdateProfileRes',
  full_name='api.UpdateProfileRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='updated_name', full_name='api.UpdateProfileRes.updated_name', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_city', full_name='api.UpdateProfileRes.updated_city', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_gender', full_name='api.UpdateProfileRes.updated_gender', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_occupation', full_name='api.UpdateProfileRes.updated_occupation', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_about_me', full_name='api.UpdateProfileRes.updated_about_me', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_about_place', full_name='api.UpdateProfileRes.updated_about_place', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_languages', full_name='api.UpdateProfileRes.updated_languages', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_countries_visited', full_name='api.UpdateProfileRes.updated_countries_visited', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_countries_lived', full_name='api.UpdateProfileRes.updated_countries_lived', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1155,
  serialized_end=1419,
)

_USER.fields_by_name['joined'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_USER.fields_by_name['last_active'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_UPDATEPROFILEREQ_REPEATEDSTRINGVALUE.containing_type = _UPDATEPROFILEREQ
_UPDATEPROFILEREQ.fields_by_name['name'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_UPDATEPROFILEREQ.fields_by_name['city'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_UPDATEPROFILEREQ.fields_by_name['gender'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_UPDATEPROFILEREQ.fields_by_name['occupation'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_UPDATEPROFILEREQ.fields_by_name['about_me'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_UPDATEPROFILEREQ.fields_by_name['about_place'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_UPDATEPROFILEREQ.fields_by_name['languages'].message_type = _UPDATEPROFILEREQ_REPEATEDSTRINGVALUE
_UPDATEPROFILEREQ.fields_by_name['countries_visited'].message_type = _UPDATEPROFILEREQ_REPEATEDSTRINGVALUE
_UPDATEPROFILEREQ.fields_by_name['countries_lived'].message_type = _UPDATEPROFILEREQ_REPEATEDSTRINGVALUE
DESCRIPTOR.message_types_by_name['PingReq'] = _PINGREQ
DESCRIPTOR.message_types_by_name['PingRes'] = _PINGRES
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['GetUserReq'] = _GETUSERREQ
DESCRIPTOR.message_types_by_name['UpdateProfileReq'] = _UPDATEPROFILEREQ
DESCRIPTOR.message_types_by_name['UpdateProfileRes'] = _UPDATEPROFILERES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PingReq = _reflection.GeneratedProtocolMessageType('PingReq', (_message.Message,), {
  'DESCRIPTOR' : _PINGREQ,
  '__module__' : 'pb.api_pb2'
  # @@protoc_insertion_point(class_scope:api.PingReq)
  })
_sym_db.RegisterMessage(PingReq)

PingRes = _reflection.GeneratedProtocolMessageType('PingRes', (_message.Message,), {
  'DESCRIPTOR' : _PINGRES,
  '__module__' : 'pb.api_pb2'
  # @@protoc_insertion_point(class_scope:api.PingRes)
  })
_sym_db.RegisterMessage(PingRes)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), {
  'DESCRIPTOR' : _USER,
  '__module__' : 'pb.api_pb2'
  # @@protoc_insertion_point(class_scope:api.User)
  })
_sym_db.RegisterMessage(User)

GetUserReq = _reflection.GeneratedProtocolMessageType('GetUserReq', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERREQ,
  '__module__' : 'pb.api_pb2'
  # @@protoc_insertion_point(class_scope:api.GetUserReq)
  })
_sym_db.RegisterMessage(GetUserReq)

UpdateProfileReq = _reflection.GeneratedProtocolMessageType('UpdateProfileReq', (_message.Message,), {

  'RepeatedStringValue' : _reflection.GeneratedProtocolMessageType('RepeatedStringValue', (_message.Message,), {
    'DESCRIPTOR' : _UPDATEPROFILEREQ_REPEATEDSTRINGVALUE,
    '__module__' : 'pb.api_pb2'
    # @@protoc_insertion_point(class_scope:api.UpdateProfileReq.RepeatedStringValue)
    })
  ,
  'DESCRIPTOR' : _UPDATEPROFILEREQ,
  '__module__' : 'pb.api_pb2'
  # @@protoc_insertion_point(class_scope:api.UpdateProfileReq)
  })
_sym_db.RegisterMessage(UpdateProfileReq)
_sym_db.RegisterMessage(UpdateProfileReq.RepeatedStringValue)

UpdateProfileRes = _reflection.GeneratedProtocolMessageType('UpdateProfileRes', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPROFILERES,
  '__module__' : 'pb.api_pb2'
  # @@protoc_insertion_point(class_scope:api.UpdateProfileRes)
  })
_sym_db.RegisterMessage(UpdateProfileRes)



_API = _descriptor.ServiceDescriptor(
  name='API',
  full_name='api.API',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1422,
  serialized_end=1571,
  methods=[
  _descriptor.MethodDescriptor(
    name='Ping',
    full_name='api.API.Ping',
    index=0,
    containing_service=None,
    input_type=_PINGREQ,
    output_type=_PINGRES,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetUser',
    full_name='api.API.GetUser',
    index=1,
    containing_service=None,
    input_type=_GETUSERREQ,
    output_type=_USER,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateProfile',
    full_name='api.API.UpdateProfile',
    index=2,
    containing_service=None,
    input_type=_UPDATEPROFILEREQ,
    output_type=_UPDATEPROFILERES,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_API)

DESCRIPTOR.services_by_name['API'] = _API

# @@protoc_insertion_point(module_scope)
