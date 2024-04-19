import os
import json
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545/'))

contract_address = Web3.to_checksum_address("0xe7f1725e7734ce288f8367e1bb143e90bb3f0512")
current_directory = os.path.dirname(os.path.abspath(__file__))
contract_abi_file = f"{current_directory}/contract_abi.json"
with open(contract_abi_file, "r") as json_file:
    abi = json.load(json_file)

contract = w3.eth.contract(address=contract_address, abi=abi)

## Call function
token_id = 0
token_uri = contract.functions.tokenURI(token_id).call()
print(f"token_uri: {token_uri}")