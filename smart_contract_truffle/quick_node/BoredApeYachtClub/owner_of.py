import os
import json
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://silent-powerful-sunset.quiknode.pro/1b4b2ca8e8106b992d01400a71e0ba35810091e2/'))

contract_address = "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D"
contract_abi_file = f"{os.getcwd()}/quick_node/contract_abi.json"
with open(contract_abi_file, "r") as json_file:
    abi = json.load(json_file)

contract = w3.eth.contract(address=contract_address, abi=abi)

## Call function
token_id = 0
owner = contract.functions.ownerOf(token_id).call()
print(f"owner: {owner}")