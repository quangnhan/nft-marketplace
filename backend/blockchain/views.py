import os
from typing import cast
from web3 import Web3
from django.http import HttpResponse
from django.shortcuts import HttpResponse, get_object_or_404
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.detail import DetailView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from blockchain import blockchain_factory
from blockchain.blockchain_factory.blockchain_factory import BlockchainFactory
from blockchain.blockchain_factory.enums.blockchain import Blockchain
from .forms import SmartContractDownloadForm
from .models import Network, SmartContract, NFT

class NetworkLatestBlockNumberView(PermissionRequiredMixin, DetailView):
    permission_required = "blockchain.view_network"
    template_name = "admin/blockchain/network/latest_block_number.html"
    model = Network

    def post(self, request, *args, **kwargs):
        network = cast(Network, self.get_object())
        try:
            blockchain_factory = BlockchainFactory.create(network.blockchain, network.network, network.rpc_server)
            latest_block_number = blockchain_factory.get_block_number()
            return render(request, self.template_name, {'latest_block_number': latest_block_number, 'object': network})
        except Exception as e:
            error_message = f"Failed to retrieve latest block number: {str(e)}"
            return render(request, self.template_name, {'error_message': error_message})
        
def save_nft_owner(request):
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
        }.items() if value == None]

        if missing_params:
            error_msg = f"Missing required parameter(s): {', '.join(missing_params)}."
            return HttpResponse(error_msg, status=400)

        if from_token_id >= to_token_id:
            return HttpResponse(f"You need to input to_token_id greater than from_token_id", status=400)

        # Retrieve the SmartContract instance
        smart_contract = get_object_or_404(SmartContract, address=smart_contract_address)

        # Initialize Web3
        http_provider = os.environ.get('BLOCKCHAIN_HTTP_PROVIDER')
        w3 = Web3(Web3.HTTPProvider(http_provider))
        
        # Retrieve the contract instance
        contract = w3.eth.contract(address=smart_contract.address, abi=smart_contract.abi) # type: ignore

        for token_id in range(from_token_id, to_token_id):
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
            if not created:
                nft.owner = owner
                nft.save()

        return HttpResponse("NFT data saved successfully.")
    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}", status=500)

class SmarContractDownloadView(PermissionRequiredMixin, DetailView):
    permission_required = "blockchain.view_smartcontract"
    template_name = "admin/blockchain/smartcontract/download.html"
    model = SmartContract

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SmartContractDownloadForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = SmartContractDownloadForm(request.POST)
        if form.is_valid():
            from_token_id = form.cleaned_data['from_token_id']
            to_token_id = form.cleaned_data['to_token_id']

            # Handle download logic here
            smart_contract = self.get_object()
        
            # Initialize Web3
            http_provider = os.environ.get('BLOCKCHAIN_HTTP_PROVIDER')
            w3 = Web3(Web3.HTTPProvider(http_provider))
            
            # Retrieve the contract instance
            contract = w3.eth.contract(address=smart_contract.address, abi=smart_contract.abi) # type: ignore

            for token_id in range(from_token_id, to_token_id):
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
                if not created:
                    nft.owner = owner
                    nft.save()

            # Return HTTP response for file download
            return redirect(reverse_lazy('admin:blockchain_smartcontract_changelist'))
        else:
            return render(request, self.template_name, {'form': form})