import os
import json
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545/'))

contract_address = Web3.to_checksum_address("0x5fc8d32690cc91d4c39d9d3abcbd16989f875707")
current_directory = os.path.dirname(os.path.abspath(__file__))
contract_abi_file = f"{current_directory}/contract_abi.json"
with open(contract_abi_file, "r") as json_file:
    abi = json.load(json_file)

contract = w3.eth.contract(address=contract_address, abi=abi)
nextTokenId = contract.functions.nextTokenId().call()

print(f"Contract nextTokenId: {nextTokenId}")