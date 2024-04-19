import os
import json
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://sepolia.infura.io/v3/6a68b19220cb4e48ab35c971af5fda20'))

contract_address = "0xb9a749EbA1Fee7685a29420a626e25d3dE539ffA"
current_directory = os.path.dirname(os.path.abspath(__file__))
contract_abi_file = f"{current_directory}/contract_abi.json"
with open(contract_abi_file, "r") as json_file:
    abi = json.load(json_file)

contract = w3.eth.contract(address=contract_address, abi=abi)
name = contract.functions.name().call()

print(f"Contract name: {name}")