from rest_framework import serializers
from blockchain.models import SmartContract

class CollectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmartContract
        fields = ('id', 'blockchain', 'network', 'name', 'token_symbol', 'address', 'image_url')