import json
from web3 import Web3
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import HttpResponse, get_object_or_404
from .models import SmartContract, NFT

def get_latest_block_number(request):
    w3 = Web3(Web3.HTTPProvider("https://silent-powerful-sunset.quiknode.pro/1b4b2ca8e8106b992d01400a71e0ba35810091e2/"))

    if not w3.is_connected():
        return HttpResponse("Failed to connect to the HTTP provider!")

    latest_block_number = w3.eth.block_number

    return HttpResponse(f"Latest Block Number: {latest_block_number}")

def save_nft_data(request):
    try:
        # Get data
        smart_contract_address = request.GET.get("smart_contract_address", None)
        from_token_id = int(request.GET.get("from_token_id", None))
        to_token_id = int(request.GET.get("to_token_id", None))

        # Check if required parameters are missing
        missing_params = [param for param, value in {
            "smart_contract_address": smart_contract_address,
            "from_token_id": from_token_id,
            "to_token_id": to_token_id
        }.items() if not value]

        if missing_params:
            error_msg = f"Missing required parameter(s): {', '.join(missing_params)}."
            return HttpResponse(error_msg, status=400)

        if from_token_id >= to_token_id:
            return HttpResponse(f"You need to input to_token_id greater than from_token_id", status=400)

        # Retrieve the SmartContract instance
        smart_contract = get_object_or_404(SmartContract, address=smart_contract_address)
        file_path = f"{settings.BASE_DIR}/{smart_contract.contract_abi_json}"
        with open(file_path, "r") as json_file:
            abi = json.load(json_file)

        # Initialize Web3
        w3 = Web3(Web3.HTTPProvider('https://silent-powerful-sunset.quiknode.pro/1b4b2ca8e8106b992d01400a71e0ba35810091e2/'))
        
        # Retrieve the contract instance
        contract = w3.eth.contract(address=smart_contract.address, abi=abi)

        for token_id in range(from_token_id, to_token_id):
            # Call the Ethereum contract function to get NFT owner
            owner = contract.functions.ownerOf(token_id).call()

            # Save NFT data to the NFT table
            nft = NFT.objects.create(
                smart_contract=smart_contract,
                owner=owner,
                token_id=token_id
            )

        return HttpResponse("NFT data saved successfully.")
    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}", status=500)