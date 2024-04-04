from django.contrib import admin
from .models import Chain, SmartContract, NFT

# Define custom admin classes if needed
class ChainAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol', 'network')

class SmartContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'chain', 'address')

class NFTAdmin(admin.ModelAdmin):
    list_display = ('smart_contract', 'owner', 'token_id', 'image_url')

# Register your models with the admin site
admin.site.register(Chain, ChainAdmin)
admin.site.register(SmartContract, SmartContractAdmin)
admin.site.register(NFT, NFTAdmin)

# Django admin
admin.site.site_header = "Admin"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome"