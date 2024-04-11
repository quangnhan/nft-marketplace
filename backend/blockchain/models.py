import json
from django.db import models
from django.core.exceptions import ValidationError
from blockchain.blockchain_factory.chain_factory import ChainFactory
from blockchain.blockchain_factory.enums.blockchain import Blockchain
from blockchain.blockchain_factory.enums.network import Network

class SmartContract(models.Model):
    NETWORK_CHOICES = [(choice.name, choice.value) for choice in Network]
    BLOCKCHAIN_CHOICES = [(choice.name, choice.value) for choice in Blockchain]

    blockchain = models.CharField(max_length=50, choices=BLOCKCHAIN_CHOICES, default=Blockchain.ETHEREUM.value)
    network = models.CharField(max_length=50, choices=NETWORK_CHOICES, default=Network.MAINNET.value)
    name = models.CharField(max_length=50, default='')
    token_symbol = models.CharField(max_length=50, default='')
    address = models.CharField(max_length=50, unique=True)
    abi = models.JSONField()
    image_url = models.URLField(default="")

    def __str__(self):
        return f"{self.blockchain}"

    def clean(self):
        super().clean()
        # self.validate_abi()
        self.validate_chain_and_network()

    def validate_abi(self):
        try:
            json.loads(self.abi)
        except json.JSONDecodeError as e:
            raise ValidationError("ABI field must be a valid JSON string.")

    def validate_chain_and_network(self):
        try:
            chain = ChainFactory.create(self.blockchain, self.network)
        except Exception as e:
            raise ValidationError(f"Failed to create chain instance: {e}")

        # Get contract name and save to database
        contract_name = chain.get_contract_name(self.address, self.abi)
        print("validate_chain_and_network", contract_name)
        if contract_name:
            self.name = contract_name
        
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