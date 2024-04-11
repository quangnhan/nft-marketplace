from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from api.serializers import CollectionListSerializer
from blockchain.models import SmartContract

# Create your views here.

class TestAPIView(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse({
            "is_machine": False,
        })
    
class CollectionListAPIView(ListAPIView):
    permission_classes = ()
    queryset = SmartContract.objects.all()
    serializer_class = CollectionListSerializer