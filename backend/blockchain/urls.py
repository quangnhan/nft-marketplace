from django.urls import path
from .views import get_latest_block_number, save_nft_owner

urlpatterns = [
    path('latest-block/', get_latest_block_number, name='blockchain-latest-block'),
    path('save-nft-owner/', save_nft_owner, name='blockchain-save-nft-data'),
]
