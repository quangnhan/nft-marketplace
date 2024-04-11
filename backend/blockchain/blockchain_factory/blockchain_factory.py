from .ethereum import Ethereum
from blockchain.blockchain_factory.enums.blockchain import Blockchain
from blockchain.blockchain_factory.enums.network import Network

class BlockchainFactory:
    @staticmethod
    def create(chain_name: str, network: str):
        chain_name_enum = getattr(Blockchain, chain_name)
        network_enum = getattr(Network, network)

        if chain_name_enum == Blockchain.ETHEREUM:
            return Ethereum(chain_name_enum, network_enum)
        else:
            raise ValueError(f"Unsupported chain: {chain_name}")
