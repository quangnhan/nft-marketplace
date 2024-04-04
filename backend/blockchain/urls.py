from django.urls import path
from .views import get_latest_block_number, save_nft_data

urlpatterns = [
    path('latest-block/', get_latest_block_number, name='blockchain-latest-block'),
    path('save-nft-data/', save_nft_data, name='blockchain-save-nft-data'),
]
