import os
from web3 import Web3
from dotenv import load_dotenv
from blockchain.blockchain_factory.enums.blockchain import Blockchain
from .base_chain import BaseChain, Network

load_dotenv()

class Ethereum(BaseChain):
    http_provide = ''

    def __init__(self, name: Blockchain, network: Network):
        super().__init__(name, network)

        if network == Network.MAINNET:
            self.http_provider = os.environ.get('BLOCKCHAIN_HTTP_PROVIDER')

    def get_contract_name(self, address: str, abi) -> str|None:
        try:
            # Fetch HTTP provider from environment variable
            if not self.http_provider:
                raise FileNotFoundError("BLOCKCHAIN_HTTP_PROVIDER environment variable is not set.")
            
            # Initialize Web3 instance
            w3 = Web3(Web3.HTTPProvider(self.http_provider))

            # Get contract instance
            contract = w3.eth.contract(address=address, abi=abi) # type: ignore
            
            # Get contract name
            name = contract.functions.name().call()

            return name
        except Exception as e:
            # Catch any other exception that might occur
            return None