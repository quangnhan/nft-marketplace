import requests
from django.core.cache import cache

class APIDataFetcher:
    def fetch_data(self, uri):
        cache_key = f"nft_data_{uri}"
        data = cache.get(cache_key)
        if data is None:
            response = requests.get(uri)
            if response.status_code == 200:
                data = response.json()
                cache.set(cache_key, data, timeout=3600)  # Cache for 1 hour
        return data

    def fetch_image_url(self, uri):
        data = self.fetch_data(uri)
        if data:
            return data.get('image')
        return None
