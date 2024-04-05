import requests

# Define the base URL
base_url = "https://api.etherscan.io/api"

# Define parameters
contract_address = "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D"
api_key = "8H7E7SYE4S5RIEDNT786SZI2A6T6P42XP3"
params = {
    "module": "contract",
    "action": "getcontractcreation",
    "contractaddresses": contract_address,
    "apikey": api_key
}

# Make the request
response = requests.get(base_url, params=params)

# Check if request was successful
if response.status_code == 200:
    data = response.json()
    print(data)  # Output the response data
else:
    print("Error:", response.status_code)
