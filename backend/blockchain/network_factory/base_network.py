from abc import ABC, abstractmethod
from blockchain.network_factory.enums.network_name import NetworkName
from blockchain.network_factory.enums.network_type import NetworkType

class BaseNetwork(ABC):
    def __init__(self, network_name: NetworkName, rpc_server: str, network_type = NetworkType):
        self.network_name = network_name
        self.rpc_server = rpc_server
        self.network_type = network_type

    @abstractmethod
    def get_block_number() -> int:
        pass
    
    @abstractmethod
    def get_contract_name(self, address: str) -> str:
        pass

    @abstractmethod
    def get_owner_of(self, address: str, abi, token_id: int) -> str:
        pass

    @abstractmethod
    def get_token_uri(self, address: str, abi, token_id: int) -> str:
        pass