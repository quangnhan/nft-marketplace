from web3 import Web3

w3 = Web3(Web3.HTTPProvider("https://polygon.drpc.org"))

if not w3.is_connected():
  print("Failed to connect to the HTTP provider!")
  exit()

latest_block_number = w3.eth.block_number

print(f"Latest Block Number: {latest_block_number}")