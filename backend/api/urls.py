from django.urls import path
from .views import SmartContractListAPIView, SmartContractDetailAPIView, NFTListAPIView, NFTDetailAPIView

urlpatterns = [
    path('smartcontracts/', SmartContractListAPIView.as_view(), name='api-smartcontract-list'),
    path('smartcontract/<str:address>/', SmartContractDetailAPIView.as_view(), name='api-smartcontract-detail'),
    path('smartcontract/<str:address>/nfts/', NFTListAPIView.as_view(), name='api-nft-list'),
    path('smartcontract/<str:address>/nft/<str:token_id>/', NFTDetailAPIView.as_view(), name='api-nft-detail'),
]
