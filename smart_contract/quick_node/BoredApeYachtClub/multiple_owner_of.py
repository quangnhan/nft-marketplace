import os
import json
from web3 import Web3

# w3 = Web3(Web3.HTTPProvider('https://silent-powerful-sunset.quiknode.pro/1b4b2ca8e8106b992d01400a71e0ba35810091e2/'))
w3 = Web3(Web3.HTTPProvider('https://eth.drpc.org'))

contract_address = "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D"
current_directory = os.path.dirname(os.path.abspath(__file__))
contract_abi_file = f"{current_directory}/contract_abi.json"
with open(contract_abi_file, "r") as json_file:
    abi = json.load(json_file)

contract = w3.eth.contract(address=contract_address, abi=abi)

## Call function
for token_id in range(0, 100):
    owner = contract.functions.ownerOf(token_id).call()
    print(f"token_id: {token_id} - owner: {owner}")