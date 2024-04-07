# tasks.py

import os
import json
from celery import shared_task
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from web3 import Web3
from .models import SmartContract, NFT

@shared_task
def save_nft_owner(smart_contract_address, from_token_id, to_token_id):
    if from_token_id >= to_token_id:
        error_msg = f"You need to input to_token_id: {to_token_id} greater than from_token_id: {from_token_id}"
        raise ValidationError(error_msg)

    # Retrieve the SmartContract instance
    smart_contract = get_object_or_404(SmartContract, address=smart_contract_address)
    file_path = f"{settings.BASE_DIR}/{smart_contract.contract_abi_json}"
    with open(file_path, "r") as json_file:
        abi = json.load(json_file)

    # Initialize Web3
    http_provider = os.environ.get('BLOCKCHAIN_HTTP_PROVIDER')
    w3 = Web3(Web3.HTTPProvider(http_provider))
    
    # Retrieve the contract instance
    contract = w3.eth.contract(address=smart_contract.address, abi=abi)
    nft_total = 0
    nft_created = 0
    nft_updated = 0

    for token_id in range(from_token_id, to_token_id):
        try:
            # Call the Ethereum contract function to get NFT owner
            owner = contract.functions.ownerOf(token_id).call()

            # Get existing NFT or create a new one if it doesn't exist
            nft, created = NFT.objects.get_or_create(
                smart_contract=smart_contract,
                token_id=token_id,
                defaults={'owner': owner}
            )
            print(f"Token id: {token_id} - Owner: {owner}")

            # If the NFT already exists, update the owner
            nft_total += 1
            if created:
                nft_created += 1
            elif nft.owner != owner:
                nft_updated += 1
                nft.owner = owner
                nft.save()
        except:
            pass
    return f"Total NFT: {nft_total}. New NFT: {nft_created}. Updated NFT: {nft_updated}"
 
