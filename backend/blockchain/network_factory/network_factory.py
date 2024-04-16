from blockchain.network_factory.polygon import Polygon
from .ethereum import Ethereum
from blockchain.network_factory.enums.network_name import NetworkName
from blockchain.network_factory.enums.network_type import NetworkType

class NetworkFactory:
    @staticmethod
    def create(chain_name: str, rpc_server: str):
        chain_name_enum = getattr(NetworkName, chain_name)

        if chain_name_enum == NetworkName.ETHEREUM:
            return Ethereum(chain_name_enum, rpc_server)
        elif chain_name_enum == NetworkName.POLYGON:
            return Polygon(chain_name_enum, rpc_server)
        else:
            raise ValueError(f"Unsupported chain: {chain_name}")
