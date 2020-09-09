# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: depscloud/api/v1beta/manifest.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='depscloud/api/v1beta/manifest.proto',
  package='depscloud.api.v1beta',
  syntax='proto3',
  serialized_options=b'Z\037github.com/depscloud/api/v1beta',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n#depscloud/api/v1beta/manifest.proto\x12\x14\x64\x65pscloud.api.v1beta\"N\n\x12ManifestDependency\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1a\n\x12version_constraint\x18\x02 \x01(\t\x12\x0e\n\x06scopes\x18\x03 \x03(\t\"\xa3\x01\n\x0cManifestFile\x12\x10\n\x08language\x18\x01 \x01(\t\x12\x0e\n\x06system\x18\x02 \x01(\t\x12\x12\n\nsource_url\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x0f\n\x07version\x18\x05 \x01(\t\x12>\n\x0c\x64\x65pendencies\x18\x06 \x03(\x0b\x32(.depscloud.api.v1beta.ManifestDependency\"0\n\x0cMatchRequest\x12\x11\n\tseparator\x18\x01 \x01(\t\x12\r\n\x05paths\x18\x02 \x03(\t\"&\n\rMatchResponse\x12\x15\n\rmatched_paths\x18\x01 \x03(\t\"\xa7\x01\n\x0e\x45xtractRequest\x12\x11\n\tseparator\x18\x01 \x01(\t\x12M\n\rfile_contents\x18\x02 \x03(\x0b\x32\x36.depscloud.api.v1beta.ExtractRequest.FileContentsEntry\x1a\x33\n\x11\x46ileContentsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"M\n\x0f\x45xtractResponse\x12:\n\x0emanifest_files\x18\x01 \x03(\x0b\x32\".depscloud.api.v1beta.ManifestFile\"r\n\x0cStoreRequest\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x0b\n\x03ref\x18\x02 \x01(\t\x12\x0c\n\x04kind\x18\x03 \x01(\t\x12:\n\x0emanifest_files\x18\x04 \x03(\x0b\x32\".depscloud.api.v1beta.ManifestFile\"\x0f\n\rStoreResponse2\xc5\x01\n\x19ManifestExtractionService\x12P\n\x05Match\x12\".depscloud.api.v1beta.MatchRequest\x1a#.depscloud.api.v1beta.MatchResponse\x12V\n\x07\x45xtract\x12$.depscloud.api.v1beta.ExtractRequest\x1a%.depscloud.api.v1beta.ExtractResponse2j\n\x16ManifestStorageService\x12P\n\x05Store\x12\".depscloud.api.v1beta.StoreRequest\x1a#.depscloud.api.v1beta.StoreResponseB!Z\x1fgithub.com/depscloud/api/v1betab\x06proto3'
)




_MANIFESTDEPENDENCY = _descriptor.Descriptor(
  name='ManifestDependency',
  full_name='depscloud.api.v1beta.ManifestDependency',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='depscloud.api.v1beta.ManifestDependency.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version_constraint', full_name='depscloud.api.v1beta.ManifestDependency.version_constraint', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scopes', full_name='depscloud.api.v1beta.ManifestDependency.scopes', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=61,
  serialized_end=139,
)


_MANIFESTFILE = _descriptor.Descriptor(
  name='ManifestFile',
  full_name='depscloud.api.v1beta.ManifestFile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='language', full_name='depscloud.api.v1beta.ManifestFile.language', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='system', full_name='depscloud.api.v1beta.ManifestFile.system', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source_url', full_name='depscloud.api.v1beta.ManifestFile.source_url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='depscloud.api.v1beta.ManifestFile.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='depscloud.api.v1beta.ManifestFile.version', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dependencies', full_name='depscloud.api.v1beta.ManifestFile.dependencies', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=142,
  serialized_end=305,
)


_MATCHREQUEST = _descriptor.Descriptor(
  name='MatchRequest',
  full_name='depscloud.api.v1beta.MatchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='separator', full_name='depscloud.api.v1beta.MatchRequest.separator', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='paths', full_name='depscloud.api.v1beta.MatchRequest.paths', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=307,
  serialized_end=355,
)


_MATCHRESPONSE = _descriptor.Descriptor(
  name='MatchResponse',
  full_name='depscloud.api.v1beta.MatchResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='matched_paths', full_name='depscloud.api.v1beta.MatchResponse.matched_paths', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=357,
  serialized_end=395,
)


_EXTRACTREQUEST_FILECONTENTSENTRY = _descriptor.Descriptor(
  name='FileContentsEntry',
  full_name='depscloud.api.v1beta.ExtractRequest.FileContentsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='depscloud.api.v1beta.ExtractRequest.FileContentsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='depscloud.api.v1beta.ExtractRequest.FileContentsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=514,
  serialized_end=565,
)

_EXTRACTREQUEST = _descriptor.Descriptor(
  name='ExtractRequest',
  full_name='depscloud.api.v1beta.ExtractRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='separator', full_name='depscloud.api.v1beta.ExtractRequest.separator', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='file_contents', full_name='depscloud.api.v1beta.ExtractRequest.file_contents', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_EXTRACTREQUEST_FILECONTENTSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=398,
  serialized_end=565,
)


_EXTRACTRESPONSE = _descriptor.Descriptor(
  name='ExtractResponse',
  full_name='depscloud.api.v1beta.ExtractResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='manifest_files', full_name='depscloud.api.v1beta.ExtractResponse.manifest_files', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=567,
  serialized_end=644,
)


_STOREREQUEST = _descriptor.Descriptor(
  name='StoreRequest',
  full_name='depscloud.api.v1beta.StoreRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='depscloud.api.v1beta.StoreRequest.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ref', full_name='depscloud.api.v1beta.StoreRequest.ref', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='kind', full_name='depscloud.api.v1beta.StoreRequest.kind', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='manifest_files', full_name='depscloud.api.v1beta.StoreRequest.manifest_files', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=646,
  serialized_end=760,
)


_STORERESPONSE = _descriptor.Descriptor(
  name='StoreResponse',
  full_name='depscloud.api.v1beta.StoreResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
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
  serialized_start=762,
  serialized_end=777,
)

_MANIFESTFILE.fields_by_name['dependencies'].message_type = _MANIFESTDEPENDENCY
_EXTRACTREQUEST_FILECONTENTSENTRY.containing_type = _EXTRACTREQUEST
_EXTRACTREQUEST.fields_by_name['file_contents'].message_type = _EXTRACTREQUEST_FILECONTENTSENTRY
_EXTRACTRESPONSE.fields_by_name['manifest_files'].message_type = _MANIFESTFILE
_STOREREQUEST.fields_by_name['manifest_files'].message_type = _MANIFESTFILE
DESCRIPTOR.message_types_by_name['ManifestDependency'] = _MANIFESTDEPENDENCY
DESCRIPTOR.message_types_by_name['ManifestFile'] = _MANIFESTFILE
DESCRIPTOR.message_types_by_name['MatchRequest'] = _MATCHREQUEST
DESCRIPTOR.message_types_by_name['MatchResponse'] = _MATCHRESPONSE
DESCRIPTOR.message_types_by_name['ExtractRequest'] = _EXTRACTREQUEST
DESCRIPTOR.message_types_by_name['ExtractResponse'] = _EXTRACTRESPONSE
DESCRIPTOR.message_types_by_name['StoreRequest'] = _STOREREQUEST
DESCRIPTOR.message_types_by_name['StoreResponse'] = _STORERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ManifestDependency = _reflection.GeneratedProtocolMessageType('ManifestDependency', (_message.Message,), {
  'DESCRIPTOR' : _MANIFESTDEPENDENCY,
  '__module__' : 'depscloud.api.v1beta.manifest_pb2'
  # @@protoc_insertion_point(class_scope:depscloud.api.v1beta.ManifestDependency)
  })
_sym_db.RegisterMessage(ManifestDependency)

ManifestFile = _reflection.GeneratedProtocolMessageType('ManifestFile', (_message.Message,), {
  'DESCRIPTOR' : _MANIFESTFILE,
  '__module__' : 'depscloud.api.v1beta.manifest_pb2'
  # @@protoc_insertion_point(class_scope:depscloud.api.v1beta.ManifestFile)
  })
_sym_db.RegisterMessage(ManifestFile)

MatchRequest = _reflection.GeneratedProtocolMessageType('MatchRequest', (_message.Message,), {
  'DESCRIPTOR' : _MATCHREQUEST,
  '__module__' : 'depscloud.api.v1beta.manifest_pb2'
  # @@protoc_insertion_point(class_scope:depscloud.api.v1beta.MatchRequest)
  })
_sym_db.RegisterMessage(MatchRequest)

MatchResponse = _reflection.GeneratedProtocolMessageType('MatchResponse', (_message.Message,), {
  'DESCRIPTOR' : _MATCHRESPONSE,
  '__module__' : 'depscloud.api.v1beta.manifest_pb2'
  # @@protoc_insertion_point(class_scope:depscloud.api.v1beta.MatchResponse)
  })
_sym_db.RegisterMessage(MatchResponse)

ExtractRequest = _reflection.GeneratedProtocolMessageType('ExtractRequest', (_message.Message,), {

  'FileContentsEntry' : _reflection.GeneratedProtocolMessageType('FileContentsEntry', (_message.Message,), {
    'DESCRIPTOR' : _EXTRACTREQUEST_FILECONTENTSENTRY,
    '__module__' : 'depscloud.api.v1beta.manifest_pb2'
    # @@protoc_insertion_point(class_scope:depscloud.api.v1beta.ExtractRequest.FileContentsEntry)
    })
  ,
  'DESCRIPTOR' : _EXTRACTREQUEST,
  '__module__' : 'depscloud.api.v1beta.manifest_pb2'
  # @@protoc_insertion_point(class_scope:depscloud.api.v1beta.ExtractRequest)
  })
_sym_db.RegisterMessage(ExtractRequest)
_sym_db.RegisterMessage(ExtractRequest.FileContentsEntry)

ExtractResponse = _reflection.GeneratedProtocolMessageType('ExtractResponse', (_message.Message,), {
  'DESCRIPTOR' : _EXTRACTRESPONSE,
  '__module__' : 'depscloud.api.v1beta.manifest_pb2'
  # @@protoc_insertion_point(class_scope:depscloud.api.v1beta.ExtractResponse)
  })
_sym_db.RegisterMessage(ExtractResponse)

StoreRequest = _reflection.GeneratedProtocolMessageType('StoreRequest', (_message.Message,), {
  'DESCRIPTOR' : _STOREREQUEST,
  '__module__' : 'depscloud.api.v1beta.manifest_pb2'
  # @@protoc_insertion_point(class_scope:depscloud.api.v1beta.StoreRequest)
  })
_sym_db.RegisterMessage(StoreRequest)

StoreResponse = _reflection.GeneratedProtocolMessageType('StoreResponse', (_message.Message,), {
  'DESCRIPTOR' : _STORERESPONSE,
  '__module__' : 'depscloud.api.v1beta.manifest_pb2'
  # @@protoc_insertion_point(class_scope:depscloud.api.v1beta.StoreResponse)
  })
_sym_db.RegisterMessage(StoreResponse)


DESCRIPTOR._options = None
_EXTRACTREQUEST_FILECONTENTSENTRY._options = None

_MANIFESTEXTRACTIONSERVICE = _descriptor.ServiceDescriptor(
  name='ManifestExtractionService',
  full_name='depscloud.api.v1beta.ManifestExtractionService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=780,
  serialized_end=977,
  methods=[
  _descriptor.MethodDescriptor(
    name='Match',
    full_name='depscloud.api.v1beta.ManifestExtractionService.Match',
    index=0,
    containing_service=None,
    input_type=_MATCHREQUEST,
    output_type=_MATCHRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Extract',
    full_name='depscloud.api.v1beta.ManifestExtractionService.Extract',
    index=1,
    containing_service=None,
    input_type=_EXTRACTREQUEST,
    output_type=_EXTRACTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MANIFESTEXTRACTIONSERVICE)

DESCRIPTOR.services_by_name['ManifestExtractionService'] = _MANIFESTEXTRACTIONSERVICE


_MANIFESTSTORAGESERVICE = _descriptor.ServiceDescriptor(
  name='ManifestStorageService',
  full_name='depscloud.api.v1beta.ManifestStorageService',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=979,
  serialized_end=1085,
  methods=[
  _descriptor.MethodDescriptor(
    name='Store',
    full_name='depscloud.api.v1beta.ManifestStorageService.Store',
    index=0,
    containing_service=None,
    input_type=_STOREREQUEST,
    output_type=_STORERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MANIFESTSTORAGESERVICE)

DESCRIPTOR.services_by_name['ManifestStorageService'] = _MANIFESTSTORAGESERVICE

# @@protoc_insertion_point(module_scope)
