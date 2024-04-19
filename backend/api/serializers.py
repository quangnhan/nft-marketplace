from rest_framework import serializers
from blockchain.models import SmartContract, NFT

class SmartContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmartContract
        fields = ('id', 'network', 'name', 'token_symbol', 'address')

class NFTSerializer(serializers.ModelSerializer):
    class Meta:
        model = NFT
        fields = ('id', 'smart_contract', 'owner', 'token_id', 'uri')