import traceback
from typing import cast
from web3 import Web3
from django.http import HttpResponse
from django.shortcuts import HttpResponse, get_object_or_404
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib import admin

from blockchain.network_factory.network_factory import NetworkFactory
from blockchain.network_factory.enums.network_name import NetworkName
from .forms import SmartContractDownloadForm
from .models import Network, SmartContract, NFT

class NetworkLatestBlockNumberView(PermissionRequiredMixin, DetailView):
    permission_required = "blockchain.view_network"
    template_name = "admin/blockchain/network/latest_block_number.html"
    model = Network

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            **admin.site.each_context(self.request),
            "opts": self.model._meta,
        }
    
    def post(self, request, *args, **kwargs):
        network = cast(Network, self.get_object())
        try:
            network_cls = NetworkFactory.create(network.network_name, network.rpc_server, network.network_type)
            latest_block_number = network_cls.get_block_number()
            messages.success(request, f"Latest block number: {latest_block_number}")
        except Exception as e:
            error_message = f"Failed to retrieve latest block number: {str(e)}"
            messages.error(request, error_message)
        finally:
            return redirect(request.path)

class SmarContractDownloadView(PermissionRequiredMixin, DetailView):
    permission_required = "blockchain.view_smartcontract"
    template_name = "admin/blockchain/smartcontract/download.html"
    model = SmartContract

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            **admin.site.each_context(self.request),
            "opts": self.model._meta,
            "form": SmartContractDownloadForm()
        }
    
    def post(self, request, *args, **kwargs):
        form = SmartContractDownloadForm(request.POST)
        try:
            if form.is_valid():
                from_token_id = form.cleaned_data['from_token_id']
                to_token_id = form.cleaned_data['to_token_id']

                # Handle download logic here
                smart_contract = cast(SmartContract, self.get_object())
                network = smart_contract.network
                network_cls = NetworkFactory.create(network.network_name, network.rpc_server, network.network_type)

                for token_id in range(from_token_id, to_token_id):
                    # Call the Ethereum contract function to get NFT owner
                    owner = network_cls.get_owner_of(smart_contract.address, smart_contract.abi, token_id)
                    token_uri = network_cls.get_token_uri(smart_contract.address, smart_contract.abi, token_id)

                    # Get existing NFT or create a new one if it doesn't exist
                    nft, created = NFT.objects.get_or_create(
                        smart_contract=smart_contract,
                        token_id=token_id,
                        defaults={'owner': owner, 'uri': token_uri}
                    )
                    print(f"Token id: {token_id} - Owner: {owner} - Token Uri: {token_uri}")

                    # If the NFT already exists, update the owner
                    if not created:
                        nft.owner = owner
                        nft.save()

                # Return HTTP response for file download
                messages.success(request, f"Download token from {from_token_id} to {to_token_id} success.")
            else:
                messages.error(request, f"Form invalid: {form.errors}")
        except Exception as e:
            error_message = f"Failed to retrieve NFT information: {str(e)}\n\nTraceback:\n{traceback.format_exc()}"
            messages.error(request, error_message)
        finally:
            return redirect(request.path)
        