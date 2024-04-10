from abc import ABC, abstractmethod
from blockchain.blockchain_factory.enums.blockchain import Blockchain
from blockchain.blockchain_factory.enums.network import Network

class BaseChain(ABC):
    def __init__(self, name: Blockchain, network: Network):
        self.name = name
        self.network = network

    @abstractmethod
    def get_contract_name(self, address: str) -> str|None:
        pass