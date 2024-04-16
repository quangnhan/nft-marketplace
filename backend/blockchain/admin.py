from django.contrib import admin
from django.urls import path, reverse
from django.utils.html import format_html
from .views import SmarContractDownloadView
from .models import SmartContract, NFT

class SmartContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'blockchain', 'network', 'address', 'download')

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
admin.site.register(SmartContract, SmartContractAdmin)
admin.site.register(NFT, NFTAdmin)

# Django admin
admin.site.site_header = "Admin"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome Admin Portal"