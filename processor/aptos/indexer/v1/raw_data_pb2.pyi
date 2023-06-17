from typing import ClassVar as _ClassVar
from typing import Iterable as _Iterable
from typing import Mapping as _Mapping
from typing import Optional as _Optional
from typing import Union as _Union

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf.internal import containers as _containers

from aptos.transaction.testing1.v1 import transaction_pb2 as _transaction_pb2

DESCRIPTOR: _descriptor.FileDescriptor

class GetTransactionsRequest(_message.Message):
    __slots__ = ["starting_version", "transactions_count"]
    STARTING_VERSION_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONS_COUNT_FIELD_NUMBER: _ClassVar[int]
    starting_version: int
    transactions_count: int
    def __init__(
        self,
        starting_version: _Optional[int] = ...,
        transactions_count: _Optional[int] = ...,
    ) -> None: ...

class TransactionsResponse(_message.Message):
    __slots__ = ["chain_id", "transactions"]
    CHAIN_ID_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    chain_id: int
    transactions: _containers.RepeatedCompositeFieldContainer[
        _transaction_pb2.Transaction
    ]
    def __init__(
        self,
        transactions: _Optional[
            _Iterable[_Union[_transaction_pb2.Transaction, _Mapping]]
        ] = ...,
        chain_id: _Optional[int] = ...,
    ) -> None: ...
