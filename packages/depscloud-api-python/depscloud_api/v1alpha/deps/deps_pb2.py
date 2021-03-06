# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: depscloud_api/v1alpha/deps/deps.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='depscloud_api/v1alpha/deps/deps.proto',
  package='cloud.deps.api.v1alpha.deps',
  syntax='proto2',
  serialized_options=b'Z%github.com/depscloud/api/v1alpha/deps',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n%depscloud_api/v1alpha/deps/deps.proto\x12\x1b\x63loud.deps.api.v1alpha.deps\"s\n\nDependency\x12\x18\n\x0corganization\x18\x01 \x01(\tB\x02\x18\x01\x12\x12\n\x06module\x18\x02 \x01(\tB\x02\x18\x01\x12\x19\n\x11versionConstraint\x18\x03 \x01(\t\x12\x0e\n\x06scopes\x18\x04 \x03(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\"\xdb\x01\n\x18\x44\x65pendencyManagementFile\x12\x10\n\x08language\x18\x01 \x01(\t\x12\x0e\n\x06system\x18\x02 \x01(\t\x12\x11\n\tsourceUrl\x18\x03 \x01(\t\x12\x18\n\x0corganization\x18\x05 \x01(\tB\x02\x18\x01\x12\x12\n\x06module\x18\x06 \x01(\tB\x02\x18\x01\x12\x0f\n\x07version\x18\x07 \x01(\t\x12=\n\x0c\x64\x65pendencies\x18\x08 \x03(\x0b\x32\'.cloud.deps.api.v1alpha.deps.Dependency\x12\x0c\n\x04name\x18\t \x01(\tB\'Z%github.com/depscloud/api/v1alpha/deps'
)




_DEPENDENCY = _descriptor.Descriptor(
  name='Dependency',
  full_name='cloud.deps.api.v1alpha.deps.Dependency',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='organization', full_name='cloud.deps.api.v1alpha.deps.Dependency.organization', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='module', full_name='cloud.deps.api.v1alpha.deps.Dependency.module', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='versionConstraint', full_name='cloud.deps.api.v1alpha.deps.Dependency.versionConstraint', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scopes', full_name='cloud.deps.api.v1alpha.deps.Dependency.scopes', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='cloud.deps.api.v1alpha.deps.Dependency.name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=70,
  serialized_end=185,
)


_DEPENDENCYMANAGEMENTFILE = _descriptor.Descriptor(
  name='DependencyManagementFile',
  full_name='cloud.deps.api.v1alpha.deps.DependencyManagementFile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='language', full_name='cloud.deps.api.v1alpha.deps.DependencyManagementFile.language', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='system', full_name='cloud.deps.api.v1alpha.deps.DependencyManagementFile.system', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sourceUrl', full_name='cloud.deps.api.v1alpha.deps.DependencyManagementFile.sourceUrl', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='organization', full_name='cloud.deps.api.v1alpha.deps.DependencyManagementFile.organization', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='module', full_name='cloud.deps.api.v1alpha.deps.DependencyManagementFile.module', index=4,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='cloud.deps.api.v1alpha.deps.DependencyManagementFile.version', index=5,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dependencies', full_name='cloud.deps.api.v1alpha.deps.DependencyManagementFile.dependencies', index=6,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='cloud.deps.api.v1alpha.deps.DependencyManagementFile.name', index=7,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=188,
  serialized_end=407,
)

_DEPENDENCYMANAGEMENTFILE.fields_by_name['dependencies'].message_type = _DEPENDENCY
DESCRIPTOR.message_types_by_name['Dependency'] = _DEPENDENCY
DESCRIPTOR.message_types_by_name['DependencyManagementFile'] = _DEPENDENCYMANAGEMENTFILE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Dependency = _reflection.GeneratedProtocolMessageType('Dependency', (_message.Message,), {
  'DESCRIPTOR' : _DEPENDENCY,
  '__module__' : 'depscloud_api.v1alpha.deps.deps_pb2'
  # @@protoc_insertion_point(class_scope:cloud.deps.api.v1alpha.deps.Dependency)
  })
_sym_db.RegisterMessage(Dependency)

DependencyManagementFile = _reflection.GeneratedProtocolMessageType('DependencyManagementFile', (_message.Message,), {
  'DESCRIPTOR' : _DEPENDENCYMANAGEMENTFILE,
  '__module__' : 'depscloud_api.v1alpha.deps.deps_pb2'
  # @@protoc_insertion_point(class_scope:cloud.deps.api.v1alpha.deps.DependencyManagementFile)
  })
_sym_db.RegisterMessage(DependencyManagementFile)


DESCRIPTOR._options = None
_DEPENDENCY.fields_by_name['organization']._options = None
_DEPENDENCY.fields_by_name['module']._options = None
_DEPENDENCYMANAGEMENTFILE.fields_by_name['organization']._options = None
_DEPENDENCYMANAGEMENTFILE.fields_by_name['module']._options = None
# @@protoc_insertion_point(module_scope)
