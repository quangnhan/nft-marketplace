import os
import json
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545/'))

contract_address = Web3.to_checksum_address("0x5FbDB2315678afecb367f032d93F642f64180aa3")
current_directory = os.path.dirname(os.path.abspath(__file__))
contract_abi_file = f"{current_directory}/contract_abi.json"
with open(contract_abi_file, "r") as json_file:
    abi = json.load(json_file)

contract = w3.eth.contract(address=contract_address, abi=abi)

## Mint NFT
ADDRESS = "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"
PRIVATE_KEY = "0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80"

for token_id in range(1, 101):
    to = "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"
    uri = f"https://lc2rtjgzig.execute-api.eu-west-1.amazonaws.com/prod/metadata/{token_id}"
    # Build the transaction
    tx = contract.functions.safeMint(to, uri).build_transaction({
        'gas': 2000000,  # Adjust gas limit as necessary
        'gasPrice': w3.to_wei('50', 'gwei'),  # Adjust gas price as necessary
        'nonce': w3.eth.get_transaction_count(ADDRESS),
    })
    
    # Sign the transaction
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=PRIVATE_KEY)
    
    # Send the signed transaction
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    
    print(f"Success: {token_id} - Transaction Hash: {tx_hash.hex()}")

