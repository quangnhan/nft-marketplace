from django.contrib import admin
from django.urls import path, reverse
from django.utils.html import format_html
from .views import SmarContractDownloadView, NetworkLatestBlockNumberView
from .models import Network, SmartContract, NFT

class NetworkAdmin(admin.ModelAdmin):
    list_display = ('blockchain', 'network', 'rpc_server', 'latest_block_number')

    def get_urls(self):
        return [
            path(
                "<pk>/latest_block",
                self.admin_site.admin_view(NetworkLatestBlockNumberView.as_view()),
                name=f"network_latest_block",
            ),
            *super().get_urls(),
        ]

    def latest_block_number(self, obj: Network) -> str:
        url = reverse("admin:network_latest_block", args=[obj.pk])
        return format_html(f'<a href="{url}">Latest Block Number</a>')
    
class SmartContractAdmin(admin.ModelAdmin):
    list_display = ('network', 'name', 'address', 'download')

    def get_urls(self):
        return [
            path(
                "<pk>/download",
                self.admin_site.admin_view(SmarContractDownloadView.as_view()),
                name=f"smart_contract_download",
            ),
            *super().get_urls(),
        ]

    def download(self, obj: SmartContract) -> str:
        url = reverse("admin:smart_contract_download", args=[obj.pk])
        return format_html(f'<a href="{url}">Download</a>')

class NFTAdmin(admin.ModelAdmin):
    list_display = ('token_id', 'contract', 'owner', 'image_url')

    def contract(self, obj):
        if obj.smart_contract.name:
            return obj.smart_contract.name
        else:
            obj.smart_contract.address

# Register your models with the admin site
admin.site.register(Network, NetworkAdmin)
admin.site.register(SmartContract, SmartContractAdmin)
admin.site.register(NFT, NFTAdmin)
