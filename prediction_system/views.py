from django.http import HttpResponse
from rest_framework.views import APIView
import json

api_key = '94cea4adae3c452ebd3c2ff10dd54d7c'

# Create your views here.
class TestView(APIView):
    def get(self, request):
        dict = {'message': 'Hello, Varun'}
        return HttpResponse(json.dumps(dict))

    def post(self,request):
        if request.META["HTTP_OCP_APIM_SUBSCRIPTION_KEY"] == api_key:
            dict = {'message': 'Hello, Varun'}
            return HttpResponse(json.dumps(dict), status=200)
        else:
            dict = {'message': 'Incorrect API Key'}
            return HttpResponse(json.dumps(dict), status=400)
