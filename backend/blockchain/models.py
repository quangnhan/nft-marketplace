import json
from django.db import models
from django.core.exceptions import ValidationError

class Chain(models.Model):
    DEVNET = 'DEVNET'
    TESTNET = 'TESTNET'
    MAINNET = 'MAINNET'
    NETWORK_CHOICES = [
        (DEVNET, 'Development Network'),
        (TESTNET, 'Test Network'),
        (MAINNET, 'Main Network'),
    ]

    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10)
    network = models.CharField(max_length=10, choices=NETWORK_CHOICES)

    def __str__(self):
        return f"{self.symbol} ({self.network})"

class SmartContract(models.Model):
    chain = models.ForeignKey(Chain, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50, unique=True)
    contract_abi_json = models.FileField(upload_to='static/smart_contract_abi', blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

    def clean(self):
        super().clean()
        # Access the uploaded file
        contract_abi_file = self.contract_abi_json
        if contract_abi_file:
            try:
                # Attempt to parse the file content as JSON
                contract_abi_data = json.loads(contract_abi_file.read().decode('utf-8'))
            except json.JSONDecodeError:
                # If parsing fails, raise a validation error
                raise ValidationError("The uploaded file is not in JSON format.")
    
class NFT(models.Model):
    smart_contract = models.ForeignKey(SmartContract, on_delete=models.CASCADE)
    owner = models.CharField(max_length=50)
    token_id = models.CharField(max_length=10)
    image_url = models.URLField(default="")

    class Meta:
        unique_together = (("smart_contract", "token_id"),)