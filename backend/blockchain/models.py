from django.db import models

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

class SmartContract(models.Model):
    chain = models.ForeignKey(Chain, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

class NFT(models.Model):
    smart_contract = models.ForeignKey(SmartContract, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    token_id = models.CharField(max_length=10)
    image_url = models.URLField()
