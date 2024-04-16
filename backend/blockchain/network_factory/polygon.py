from web3 import Web3
from blockchain.network_factory.enums.network_name import NetworkName
from .base_network import BaseNetwork, NetworkType

class Polygon(BaseNetwork):
    def __init__(self, network_name: NetworkName, rpc_server: str):
        super().__init__(network_name, rpc_server)
        self.w3 = Web3(Web3.HTTPProvider(rpc_server))

    def get_block_number(self) -> int:
        if not self.w3.is_connected():
            raise ConnectionError("Failed to connect to the HTTP provider!")

        latest_block_number = self.w3.eth.block_number
        return latest_block_number
    
    def get_contract_name(self, address: str, abi) -> str|None:
        try:
            # Get contract instance
            contract = self.w3.eth.contract(address=address, abi=abi) # type: ignore
            
            # Get contract name
            name = contract.functions.name().call()

            return name
        except Exception as e:
            # Catch any other exception that might occur
            return None
        
    def get_owner_of(self, address: str, abi, token_id: str) -> str | None:
        try:
            contract = self.w3.eth.contract(address=address, abi=abi) # type: ignore
            owner = contract.functions.ownerOf(token_id).call()
            return owner
        except Exception as e:
            return None