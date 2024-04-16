from abc import ABC, abstractmethod
from blockchain.network_factory.enums.network_name import NetworkName
from blockchain.network_factory.enums.network_type import NetworkType

class BaseNetwork(ABC):
    def __init__(self, network_name: NetworkName, rpc_server: str):
        self.network_name = network_name
        self.rpc_server = rpc_server

    @abstractmethod
    def get_block_number() -> int:
        pass
    
    @abstractmethod
    def get_contract_name(self, address: str) -> str|None:
        pass

    @abstractmethod
    def get_owner_of(self, address: str, abi, token_id: str) -> str|None:
        pass