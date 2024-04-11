from abc import ABC, abstractmethod
from blockchain.blockchain_factory.enums.blockchain import Blockchain
from blockchain.blockchain_factory.enums.network import Network

class BaseBlockchain(ABC):
    def __init__(self, name: Blockchain, network: Network):
        self.name = name
        self.network = network

    @abstractmethod
    def get_block_number() -> int:
        pass
    
    @abstractmethod
    def get_contract_name(self, address: str) -> str|None:
        pass

    @abstractmethod
    def get_owner_of(self, address: str, abi, token_id: str) -> str|None:
        pass