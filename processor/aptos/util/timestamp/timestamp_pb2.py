# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aptos/util/timestamp/timestamp.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n$aptos/util/timestamp/timestamp.proto\x12\x14\x61ptos.util.timestamp"+\n\tTimestamp\x12\x0f\n\x07seconds\x18\x01 \x01(\x03\x12\r\n\x05nanos\x18\x02 \x01(\x05\x62\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "aptos.util.timestamp.timestamp_pb2", globals()
)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _TIMESTAMP._serialized_start = 62
    _TIMESTAMP._serialized_end = 105
# @@protoc_insertion_point(module_scope)
