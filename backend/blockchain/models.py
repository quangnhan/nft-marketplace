import json
from django.db import models
from django.core.exceptions import ValidationError
from blockchain.blockchain_factory.enums.blockchain import Blockchain
from blockchain.blockchain_factory.enums.network import NetworkType

class Network(models.Model):
    BLOCKCHAIN_CHOICES = [(choice.name, choice.value) for choice in Blockchain]
    NETWORK_CHOICES = [(choice.name, choice.value) for choice in NetworkType]

    blockchain = models.CharField(max_length=50, choices=BLOCKCHAIN_CHOICES, default=Blockchain.ETHEREUM.value)
    network = models.CharField(max_length=50, choices=NETWORK_CHOICES, default=NetworkType.MAINNET.value)
    rpc_server = models.URLField()
    image_url = models.URLField(blank=True, default="")

    def __str__(self) -> str:
        return f"{self.blockchain} {self.network}"

class SmartContract(models.Model):
    network = models.ForeignKey(Network, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='')
    token_symbol = models.CharField(max_length=50, default='')
    address = models.CharField(max_length=50, unique=True)
    abi = models.JSONField()
    image_url = models.URLField(default="")

    def __str__(self):
        return f"{self.network} - {self.name} - {self.address}"

    def clean(self):
        super().clean()
        # self.validate_abi()

    def validate_abi(self):
        try:
            json.loads(self.abi)
        except json.JSONDecodeError as e:
            raise ValidationError("ABI field must be a valid JSON string.")
        
class NFT(models.Model):
    smart_contract = models.ForeignKey(SmartContract, on_delete=models.CASCADE)
    owner = models.CharField(max_length=50)
    token_id = models.CharField(max_length=10)
    image_url = models.URLField(default="")

    class Meta:
        unique_together = (("smart_contract", "token_id"),)

    def __str__(self):
        if self.smart_contract.name:
            return f"Contract: {self.smart_contract.name} - Token ID: {self.token_id}"
        else:
            return f"Contract: {self.smart_contract.address} - Token ID: {self.token_id}"