from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.http import Http404
from api.serializers import SmartContractSerializer, NFTSerializer
from blockchain.models import SmartContract, NFT

# Create your views here.

class SmartContractListAPIView(ListAPIView):
    permission_classes = ()
    queryset = SmartContract.objects.all()
    serializer_class = SmartContractSerializer

class SmartContractDetailAPIView(RetrieveAPIView):
    permission_classes = ()
    serializer_class = SmartContractSerializer

    def get_object(self):
        address = self.kwargs.get("address")
        try:
            smart_contract = SmartContract.objects.get(address=address)
        except SmartContract.DoesNotExist:
            raise Http404("SmartContract not found")
        return smart_contract

class NFTListAPIView(ListAPIView):
    permission_classes = ()
    serializer_class = NFTSerializer

    def get_queryset(self):
        address = self.kwargs.get("address")
        try:
            smart_contract = SmartContract.objects.get(address=address)
            nfts = NFT.objects.filter(smart_contract=smart_contract)
        except SmartContract.DoesNotExist:
            raise Http404("SmartContract not found")
        return nfts
    
class NFTDetailAPIView(RetrieveAPIView):
    permission_classes = ()
    serializer_class = NFTSerializer

    def get_object(self):
        address = self.kwargs.get("address")
        token_id = self.kwargs.get("token_id")
        try:
            smart_contract = SmartContract.objects.get(address=address)
            nft =  NFT.objects.get(smart_contract=smart_contract, token_id=token_id)
        except NFT.DoesNotExist:
            raise Http404("NFT not found")
        return nft