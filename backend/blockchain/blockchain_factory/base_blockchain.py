from abc import ABC, abstractmethod
from blockchain.blockchain_factory.enums.blockchain import Blockchain
from blockchain.blockchain_factory.enums.network import NetworkType

class BaseBlockchain(ABC):
    def __init__(self, name: Blockchain, network: NetworkType, rpc_server: str):
        self.name = name
        self.network = network
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