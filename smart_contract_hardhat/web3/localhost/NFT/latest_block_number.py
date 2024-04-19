from web3 import Web3

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545/'))

if w3.is_connected():
    latest_block_number = w3.eth.block_number
    print("latest_block_number", latest_block_number)
else:
    print("Error")
