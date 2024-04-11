from django.urls import path
from .views import TestAPIView, CollectionListAPIView

urlpatterns = [
    path('test/', TestAPIView.as_view(), name='test-api'),
    path('collections/', CollectionListAPIView.as_view(), name='api-collection-list'),
]
