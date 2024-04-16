from blockchain.blockchain_factory.polygon import Polygon
from .ethereum import Ethereum
from blockchain.blockchain_factory.enums.blockchain import Blockchain
from blockchain.blockchain_factory.enums.network import NetworkType

class BlockchainFactory:
    @staticmethod
    def create(chain_name: str, network: str, rpc_server: str):
        chain_name_enum = getattr(Blockchain, chain_name)
        network_enum = getattr(NetworkType, network)

        if chain_name_enum == Blockchain.ETHEREUM:
            return Ethereum(chain_name_enum, network_enum, rpc_server)
        elif chain_name_enum == Blockchain.POLYGON:
            return Polygon(chain_name_enum, network_enum, rpc_server)
        else:
            raise ValueError(f"Unsupported chain: {chain_name}")
