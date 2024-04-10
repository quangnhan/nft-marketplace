# tasks.py

import os
from celery import shared_task
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from web3 import Web3
from .models import SmartContract, NFT

@shared_task
def save_nft_owner(smart_contract_address, from_token_id, to_token_id):
    # Validate token range
    if from_token_id >= to_token_id:
        raise ValidationError(f"The 'to_token_id' ({to_token_id}) must be greater than 'from_token_id' ({from_token_id}).")

    # Retrieve the SmartContract instance
    smart_contract = get_object_or_404(SmartContract, address=smart_contract_address)

    # Initialize Web3
    http_provider = os.environ.get('BLOCKCHAIN_HTTP_PROVIDER')
    w3 = Web3(Web3.HTTPProvider(http_provider))
    
    # Retrieve the contract instance
    contract = w3.eth.contract(address=smart_contract.address, abi=smart_contract.abi) # type: ignore
    
    # Variables to track statistics
    nft_total = 0
    nft_created = 0
    nft_updated = 0

    # Iterate over token IDs
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

            # Update statistics
            nft_total += 1
            if created:
                nft_created += 1
            elif nft.owner != owner:
                nft_updated += 1
                nft.owner = owner
                nft.save()
            print(f"Token id: {token_id} - Owner: {owner}")
        except Exception as e:
            # Handle exceptions
            print(f"Failed to process token id {token_id}: {e}")

    return f"Total NFT: {nft_total}. New NFT: {nft_created}. Updated NFT: {nft_updated}"
 
