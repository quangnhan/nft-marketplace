import os
import json
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://eth.drpc.org'))

contract_address = "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D"
current_directory = os.path.dirname(os.path.abspath(__file__))
contract_abi_file = f"{current_directory}/contract_abi.json"
with open(contract_abi_file, "r") as json_file:
    abi = json.load(json_file)

contract = w3.eth.contract(address=contract_address, abi=abi)
name = contract.functions.name().call()

print(f"Contract name: {name}")