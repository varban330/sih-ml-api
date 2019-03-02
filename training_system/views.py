import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from django.http import HttpResponse
from rest_framework.views import APIView
import json
import pickle

api_key = '94cea4adae3c452ebd3c2ff10dd54d7c'
# Create your views here.
class TestView(APIView):
    def get(self, request):
        if request.META["HTTP_OCP_APIM_SUBSCRIPTION_KEY"] == api_key:
            dict = {'message': 'Hi,This is your developer, Varun this side'}
            return HttpResponse(json.dumps(dict),status=200)
        else:
            dict = {'message': 'Incorrect API Key'}
            return HttpResponse(json.dumps(dict), status=401)

    def post(self,request):
        if request.META["HTTP_OCP_APIM_SUBSCRIPTION_KEY"] == api_key:
            dict = {'message': 'Hi,This is your developer, Varun this side'}
            return HttpResponse(json.dumps(dict), status=200)
        else:
            dict = {'message': 'Incorrect API Key'}
            return HttpResponse(json.dumps(dict), status=401)
