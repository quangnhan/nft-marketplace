import os
from web3 import Web3
from dotenv import load_dotenv
from blockchain.blockchain_factory.enums.blockchain import Blockchain
from .base_blockchain import BaseBlockchain, Network

load_dotenv()

class Ethereum(BaseBlockchain):
    http_provide = ''

    def __init__(self, name: Blockchain, network: Network):
        super().__init__(name, network)

        if network == Network.MAINNET:
            self.http_provider = os.environ.get('BLOCKCHAIN_HTTP_PROVIDER')

        self.w3 = Web3(Web3.HTTPProvider(self.http_provider))

    def get_block_number(self) -> int:
        if not self.w3.is_connected():
            raise ConnectionError("Failed to connect to the HTTP provider!")

        latest_block_number = self.w3.eth.block_number
        return latest_block_number
    
    def get_contract_name(self, address: str, abi) -> str|None:
        try:
            # Fetch HTTP provider from environment variable
            if not self.http_provider:
                raise FileNotFoundError("BLOCKCHAIN_HTTP_PROVIDER environment variable is not set.")

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