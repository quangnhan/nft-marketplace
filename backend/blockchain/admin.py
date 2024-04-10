from django.contrib import admin
from .models import SmartContract, NFT

class SmartContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'blockchain', 'network', 'address')
    readonly_fields = ['name']

class NFTAdmin(admin.ModelAdmin):
    list_display = ('token_id', 'contract', 'owner', 'image_url')

    def contract(self, obj):
        if obj.smart_contract.name:
            return obj.smart_contract.name
        else:
            obj.smart_contract.address

# Register your models with the admin site
admin.site.register(SmartContract, SmartContractAdmin)
admin.site.register(NFT, NFTAdmin)

# Django admin
admin.site.site_header = "Admin"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome Admin Portal"