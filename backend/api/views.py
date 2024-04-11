from django.http import JsonResponse
from rest_framework.views import APIView

# Create your views here.

class TestAPIView(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse({
            "is_machine": False,
        })