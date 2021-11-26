# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: satellite/debug/larky_gateway/gateway.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='satellite/debug/larky_gateway/gateway.proto',
  package='larky_gateway',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n+satellite/debug/larky_gateway/gateway.proto\x12\rlarky_gateway\"\xb4\x01\n\x0b\x43lientEvent\x12\x35\n\x0bnew_session\x18\x65 \x01(\x0b\x32\x1e.larky_gateway.NewSessionEventH\x00\x12\x37\n\x0cresult_ready\x18\x66 \x01(\x0b\x32\x1f.larky_gateway.ResultReadyEventH\x00\x12*\n\x05\x65rror\x18g \x01(\x0b\x32\x19.larky_gateway.ErrorEventH\x00\x42\t\n\x07payload\"D\n\x0fNewSessionEvent\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\r\n\x05vault\x18\x02 \x01(\t\x12\x0e\n\x06org_id\x18\x03 \x01(\t\"D\n\x10ResultReadyEvent\x12\x30\n\x0chttp_message\x18\x01 \x01(\x0b\x32\x1a.larky_gateway.HttpMessage\"\x1d\n\nErrorEvent\x12\x0f\n\x07message\x18\x01 \x01(\t\"S\n\x0bServerEvent\x12\x39\n\rproxy_request\x18\x65 \x01(\x0b\x32 .larky_gateway.ProxyRequestEventH\x00\x42\t\n\x07payload\"[\n\x11ProxyRequestEvent\x12\x30\n\x0chttp_message\x18\x01 \x01(\x0b\x32\x1a.larky_gateway.HttpMessage\x12\x14\n\x0clarky_script\x18\x02 \x01(\t\"\x92\x01\n\x0bHttpMessage\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t\x12\x38\n\x07headers\x18\x03 \x03(\x0b\x32\'.larky_gateway.HttpMessage.HeadersEntry\x1a.\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x32Z\n\x0cLarkyGateway\x12J\n\x0c\x44\x65\x62ugSession\x12\x1a.larky_gateway.ClientEvent\x1a\x1a.larky_gateway.ServerEvent(\x01\x30\x01\x62\x06proto3'
)




_CLIENTEVENT = _descriptor.Descriptor(
  name='ClientEvent',
  full_name='larky_gateway.ClientEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='new_session', full_name='larky_gateway.ClientEvent.new_session', index=0,
      number=101, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result_ready', full_name='larky_gateway.ClientEvent.result_ready', index=1,
      number=102, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error', full_name='larky_gateway.ClientEvent.error', index=2,
      number=103, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='payload', full_name='larky_gateway.ClientEvent.payload',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=63,
  serialized_end=243,
)


_NEWSESSIONEVENT = _descriptor.Descriptor(
  name='NewSessionEvent',
  full_name='larky_gateway.NewSessionEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_id', full_name='larky_gateway.NewSessionEvent.session_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vault', full_name='larky_gateway.NewSessionEvent.vault', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='org_id', full_name='larky_gateway.NewSessionEvent.org_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=245,
  serialized_end=313,
)


_RESULTREADYEVENT = _descriptor.Descriptor(
  name='ResultReadyEvent',
  full_name='larky_gateway.ResultReadyEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='http_message', full_name='larky_gateway.ResultReadyEvent.http_message', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=315,
  serialized_end=383,
)


_ERROREVENT = _descriptor.Descriptor(
  name='ErrorEvent',
  full_name='larky_gateway.ErrorEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='larky_gateway.ErrorEvent.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=385,
  serialized_end=414,
)


_SERVEREVENT = _descriptor.Descriptor(
  name='ServerEvent',
  full_name='larky_gateway.ServerEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='proxy_request', full_name='larky_gateway.ServerEvent.proxy_request', index=0,
      number=101, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='payload', full_name='larky_gateway.ServerEvent.payload',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=416,
  serialized_end=499,
)


_PROXYREQUESTEVENT = _descriptor.Descriptor(
  name='ProxyRequestEvent',
  full_name='larky_gateway.ProxyRequestEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='http_message', full_name='larky_gateway.ProxyRequestEvent.http_message', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='larky_script', full_name='larky_gateway.ProxyRequestEvent.larky_script', index=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=501,
  serialized_end=592,
)


_HTTPMESSAGE_HEADERSENTRY = _descriptor.Descriptor(
  name='HeadersEntry',
  full_name='larky_gateway.HttpMessage.HeadersEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='larky_gateway.HttpMessage.HeadersEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='larky_gateway.HttpMessage.HeadersEntry.value', index=1,
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
  serialized_start=695,
  serialized_end=741,
)

_HTTPMESSAGE = _descriptor.Descriptor(
  name='HttpMessage',
  full_name='larky_gateway.HttpMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='larky_gateway.HttpMessage.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='larky_gateway.HttpMessage.data', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='headers', full_name='larky_gateway.HttpMessage.headers', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_HTTPMESSAGE_HEADERSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=595,
  serialized_end=741,
)

_CLIENTEVENT.fields_by_name['new_session'].message_type = _NEWSESSIONEVENT
_CLIENTEVENT.fields_by_name['result_ready'].message_type = _RESULTREADYEVENT
_CLIENTEVENT.fields_by_name['error'].message_type = _ERROREVENT
_CLIENTEVENT.oneofs_by_name['payload'].fields.append(
  _CLIENTEVENT.fields_by_name['new_session'])
_CLIENTEVENT.fields_by_name['new_session'].containing_oneof = _CLIENTEVENT.oneofs_by_name['payload']
_CLIENTEVENT.oneofs_by_name['payload'].fields.append(
  _CLIENTEVENT.fields_by_name['result_ready'])
_CLIENTEVENT.fields_by_name['result_ready'].containing_oneof = _CLIENTEVENT.oneofs_by_name['payload']
_CLIENTEVENT.oneofs_by_name['payload'].fields.append(
  _CLIENTEVENT.fields_by_name['error'])
_CLIENTEVENT.fields_by_name['error'].containing_oneof = _CLIENTEVENT.oneofs_by_name['payload']
_RESULTREADYEVENT.fields_by_name['http_message'].message_type = _HTTPMESSAGE
_SERVEREVENT.fields_by_name['proxy_request'].message_type = _PROXYREQUESTEVENT
_SERVEREVENT.oneofs_by_name['payload'].fields.append(
  _SERVEREVENT.fields_by_name['proxy_request'])
_SERVEREVENT.fields_by_name['proxy_request'].containing_oneof = _SERVEREVENT.oneofs_by_name['payload']
_PROXYREQUESTEVENT.fields_by_name['http_message'].message_type = _HTTPMESSAGE
_HTTPMESSAGE_HEADERSENTRY.containing_type = _HTTPMESSAGE
_HTTPMESSAGE.fields_by_name['headers'].message_type = _HTTPMESSAGE_HEADERSENTRY
DESCRIPTOR.message_types_by_name['ClientEvent'] = _CLIENTEVENT
DESCRIPTOR.message_types_by_name['NewSessionEvent'] = _NEWSESSIONEVENT
DESCRIPTOR.message_types_by_name['ResultReadyEvent'] = _RESULTREADYEVENT
DESCRIPTOR.message_types_by_name['ErrorEvent'] = _ERROREVENT
DESCRIPTOR.message_types_by_name['ServerEvent'] = _SERVEREVENT
DESCRIPTOR.message_types_by_name['ProxyRequestEvent'] = _PROXYREQUESTEVENT
DESCRIPTOR.message_types_by_name['HttpMessage'] = _HTTPMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientEvent = _reflection.GeneratedProtocolMessageType('ClientEvent', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTEVENT,
  '__module__' : 'satellite.debug.larky_gateway.gateway_pb2'
  # @@protoc_insertion_point(class_scope:larky_gateway.ClientEvent)
  })
_sym_db.RegisterMessage(ClientEvent)

NewSessionEvent = _reflection.GeneratedProtocolMessageType('NewSessionEvent', (_message.Message,), {
  'DESCRIPTOR' : _NEWSESSIONEVENT,
  '__module__' : 'satellite.debug.larky_gateway.gateway_pb2'
  # @@protoc_insertion_point(class_scope:larky_gateway.NewSessionEvent)
  })
_sym_db.RegisterMessage(NewSessionEvent)

ResultReadyEvent = _reflection.GeneratedProtocolMessageType('ResultReadyEvent', (_message.Message,), {
  'DESCRIPTOR' : _RESULTREADYEVENT,
  '__module__' : 'satellite.debug.larky_gateway.gateway_pb2'
  # @@protoc_insertion_point(class_scope:larky_gateway.ResultReadyEvent)
  })
_sym_db.RegisterMessage(ResultReadyEvent)

ErrorEvent = _reflection.GeneratedProtocolMessageType('ErrorEvent', (_message.Message,), {
  'DESCRIPTOR' : _ERROREVENT,
  '__module__' : 'satellite.debug.larky_gateway.gateway_pb2'
  # @@protoc_insertion_point(class_scope:larky_gateway.ErrorEvent)
  })
_sym_db.RegisterMessage(ErrorEvent)

ServerEvent = _reflection.GeneratedProtocolMessageType('ServerEvent', (_message.Message,), {
  'DESCRIPTOR' : _SERVEREVENT,
  '__module__' : 'satellite.debug.larky_gateway.gateway_pb2'
  # @@protoc_insertion_point(class_scope:larky_gateway.ServerEvent)
  })
_sym_db.RegisterMessage(ServerEvent)

ProxyRequestEvent = _reflection.GeneratedProtocolMessageType('ProxyRequestEvent', (_message.Message,), {
  'DESCRIPTOR' : _PROXYREQUESTEVENT,
  '__module__' : 'satellite.debug.larky_gateway.gateway_pb2'
  # @@protoc_insertion_point(class_scope:larky_gateway.ProxyRequestEvent)
  })
_sym_db.RegisterMessage(ProxyRequestEvent)

HttpMessage = _reflection.GeneratedProtocolMessageType('HttpMessage', (_message.Message,), {

  'HeadersEntry' : _reflection.GeneratedProtocolMessageType('HeadersEntry', (_message.Message,), {
    'DESCRIPTOR' : _HTTPMESSAGE_HEADERSENTRY,
    '__module__' : 'satellite.debug.larky_gateway.gateway_pb2'
    # @@protoc_insertion_point(class_scope:larky_gateway.HttpMessage.HeadersEntry)
    })
  ,
  'DESCRIPTOR' : _HTTPMESSAGE,
  '__module__' : 'satellite.debug.larky_gateway.gateway_pb2'
  # @@protoc_insertion_point(class_scope:larky_gateway.HttpMessage)
  })
_sym_db.RegisterMessage(HttpMessage)
_sym_db.RegisterMessage(HttpMessage.HeadersEntry)


_HTTPMESSAGE_HEADERSENTRY._options = None

_LARKYGATEWAY = _descriptor.ServiceDescriptor(
  name='LarkyGateway',
  full_name='larky_gateway.LarkyGateway',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=743,
  serialized_end=833,
  methods=[
  _descriptor.MethodDescriptor(
    name='DebugSession',
    full_name='larky_gateway.LarkyGateway.DebugSession',
    index=0,
    containing_service=None,
    input_type=_CLIENTEVENT,
    output_type=_SERVEREVENT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_LARKYGATEWAY)

DESCRIPTOR.services_by_name['LarkyGateway'] = _LARKYGATEWAY

# @@protoc_insertion_point(module_scope)
