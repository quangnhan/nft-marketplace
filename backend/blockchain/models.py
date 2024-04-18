from django.db import models
from blockchain.network_factory.enums.network_name import NetworkName
from blockchain.network_factory.enums.network_type import NetworkType

class Network(models.Model):
    NETWORK_NAME_CHOICES = [(choice.name, choice.value) for choice in NetworkName]
    NETWORK_TYPE_CHOICES = [(choice.name, choice.value) for choice in NetworkType]

    network_name = models.CharField(max_length=50, choices=NETWORK_NAME_CHOICES, default=NetworkName.ETHEREUM.value)
    network_type = models.CharField(max_length=50, choices=NETWORK_TYPE_CHOICES, default=NetworkType.MAINNET.value)
    rpc_server = models.URLField()
    image_url = models.URLField(blank=True, default="")

    def __str__(self) -> str:
        return f"[{self.network_name} {self.network_type}]"

class SmartContract(models.Model):
    network = models.ForeignKey(Network, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='', blank=True)
    token_symbol = models.CharField(max_length=50, default='', blank=True)
    address = models.CharField(max_length=50, unique=True)
    abi = models.JSONField()
    image_url = models.URLField(default="", blank=True)

    def __str__(self):
        return f"[{self.network} {self.name}]"
        
class NFT(models.Model):
    smart_contract = models.ForeignKey(SmartContract, on_delete=models.CASCADE)
    owner = models.CharField(max_length=50)
    token_id = models.CharField(max_length=10)
    uri = models.URLField(default="")
    image_url = models.URLField(default="")

    class Meta:
        unique_together = (("smart_contract", "token_id"),)

    def __str__(self):
        if self.smart_contract.name:
            return f"[{self.smart_contract.name}: TokenID {self.token_id}]"
        else:
            return f"[{self.smart_contract.address}: TokenID {self.token_id}]"