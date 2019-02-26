from django.http import HttpResponse
from rest_framework.views import APIView
import json


# Create your views here.
class Testview(APIView):
    def get(self, request):
        dict = {'message': 'Hello, Varun'}
        return HttpResponse(json.dumps(dict))

    def post(self,request):
        print(request.META["HTTP_OCP_APIM_SUBSCRIPTION_KEY"])
        dict = {'message': 'Hello, Varun'}
        return HttpResponse(json.dumps(dict))
