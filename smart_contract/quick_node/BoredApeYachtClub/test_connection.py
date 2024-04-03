from web3 import Web3

w3 = Web3(Web3.HTTPProvider("https://silent-powerful-sunset.quiknode.pro/1b4b2ca8e8106b992d01400a71e0ba35810091e2/"))

if not w3.is_connected():
  print("Failed to connect to the HTTP provider!")
  exit()

latest_block_number = w3.eth.block_number

print(f"Latest Block Number: {latest_block_number}")