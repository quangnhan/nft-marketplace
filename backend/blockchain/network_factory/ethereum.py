from web3 import Web3
from blockchain.network_factory.enums.network_name import NetworkName
from .base_network import BaseNetwork, NetworkType

class Ethereum(BaseNetwork):
    def __init__(self, network_name: NetworkName, rpc_server: str, network_type = NetworkType):
        super().__init__(network_name, rpc_server, network_type)
        self.w3 = Web3(Web3.HTTPProvider(rpc_server))

    def _protect_contract_address(self, address: str) -> str:
        if self.network_type == NetworkType.DEVNET:
            return Web3.to_checksum_address(address)
        return address

    def get_block_number(self) -> int:
        if not self.w3.is_connected():
            raise ConnectionError("Failed to connect to the HTTP provider!")

        latest_block_number = self.w3.eth.block_number
        return latest_block_number
    
    def get_contract_name(self, address: str, abi) -> str:
        contract = self.w3.eth.contract(address=address, abi=abi) # type: ignore
        name = contract.functions.name().call()
        return name
        
    def get_owner_of(self, address: str, abi, token_id: int) -> str:
        address = self._protect_contract_address(address)
        contract = self.w3.eth.contract(address=address, abi=abi) # type: ignore
        owner = contract.functions.ownerOf(token_id).call()
        return owner

    def get_token_uri(self, address: str, abi, token_id: int) -> str:
        address = self._protect_contract_address(address)
        contract = self.w3.eth.contract(address=address, abi=abi) # type: ignore
        owner = contract.functions.tokenURI(token_id).call()
        return owner