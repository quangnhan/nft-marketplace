from django.urls import path
from .views import save_nft_owner

urlpatterns = [
    path('save-nft-owner/', save_nft_owner, name='blockchain-save-nft-data'),
]
