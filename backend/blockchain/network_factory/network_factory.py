from blockchain.network_factory.polygon import Polygon
from .ethereum import Ethereum
from blockchain.network_factory.enums.network_name import NetworkName
from blockchain.network_factory.enums.network_type import NetworkType

class NetworkFactory:
    @staticmethod
    def create(network_name: str, rpc_server: str, network_type: str):
        network_name_enum = getattr(NetworkName, network_name)
        network_type_enum = getattr(NetworkType, network_type)

        if network_name_enum == NetworkName.ETHEREUM:
            return Ethereum(network_name_enum, rpc_server, network_type_enum)
        elif network_name_enum == NetworkName.POLYGON:
            return Polygon(network_name_enum, rpc_server, network_type_enum)
        else:
            raise ValueError(f"Unsupported chain: {network_name}")
