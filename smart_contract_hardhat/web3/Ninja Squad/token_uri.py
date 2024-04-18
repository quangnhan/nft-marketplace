import os
import json
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://rpc.payload.de'))

contract_address = Web3.to_checksum_address("0x8C186802b1992f7650Ac865d4CA94D55fF3C0d17")
current_directory = os.path.dirname(os.path.abspath(__file__))
contract_abi_file = f"{current_directory}/contract_abi.json"
with open(contract_abi_file, "r") as json_file:
    abi = json.load(json_file)

contract = w3.eth.contract(address=contract_address, abi=abi)

## Call function
token_id = 100
token_uri = contract.functions.tokenURI(token_id).call()
print(f"token_uri: {token_uri}")