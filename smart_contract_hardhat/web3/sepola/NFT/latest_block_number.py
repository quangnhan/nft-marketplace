from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://sepolia.infura.io/v3/6a68b19220cb4e48ab35c971af5fda20'))

if w3.is_connected():
    latest_block_number = w3.eth.block_number
    print("latest_block_number", latest_block_number)
else:
    print("Error")
