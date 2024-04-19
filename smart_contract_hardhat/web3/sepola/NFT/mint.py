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

## Mint NFT
ADDRESS = "0x5BF421d1b035a7FC4cF9436CBC42AA122A05749B"
PRIVATE_KEY = "d1a83bac1934546bab94f8a5d412ed25d1847f48e445c6756277b780c647fae2"

for token_id in range(1, 100):
    to = "0x5BF421d1b035a7FC4cF9436CBC42AA122A05749B"
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

