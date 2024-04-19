from django.contrib import admin
from django.urls import path, reverse
from django.utils.html import format_html
from .views import SmarContractDownloadView, NetworkLatestBlockNumberView
from .models import Network, SmartContract, NFT

class NetworkAdmin(admin.ModelAdmin):
    list_display = ('network_name', 'network_type', 'rpc_server', 'action')

    def get_urls(self):
        return [
            path(
                "<pk>/latest_block",
                self.admin_site.admin_view(NetworkLatestBlockNumberView.as_view()),
                name=f"network_check_connection",
            ),
            *super().get_urls(),
        ]

    def action(self, obj: Network) -> str:
        url = reverse("admin:network_check_connection", args=[obj.pk])
        return format_html(f'<a href="{url}" class="button">Check connection</a>')
    
class SmartContractAdmin(admin.ModelAdmin):
    list_display = ('network', 'name', 'token_symbol', 'address', 'action')

    def get_urls(self):
        return [
            path(
                "<pk>/download",
                self.admin_site.admin_view(SmarContractDownloadView.as_view()),
                name=f"smart_contract_download",
            ),
            *super().get_urls(),
        ]

    def action(self, obj: SmartContract) -> str:
        url = reverse("admin:smart_contract_download", args=[obj.pk])
        return format_html(f'<a href="{url}" class="button">Download NFT</a>')

class NFTAdmin(admin.ModelAdmin):
    list_display = ('network', 'contract', 'token_id', 'owner')
    list_filter = ('smart_contract__network', 'smart_contract__name', )

    def contract(self, obj):
        return obj.smart_contract.name
    
    def network(self, obj):
        return obj.smart_contract.network

# Register your models with the admin site
admin.site.register(Network, NetworkAdmin)
admin.site.register(SmartContract, SmartContractAdmin)
admin.site.register(NFT, NFTAdmin)
