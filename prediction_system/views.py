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


class MessFeePred(APIView):
    def get(self, request):
        if request.META["HTTP_OCP_APIM_SUBSCRIPTION_KEY"] == api_key:
            dict = {'message': 'Hi,This is your developer, Varun this side'}
            return HttpResponse(json.dumps(dict),status=200)
        else:
            dict = {'message': 'Incorrect API Key'}
            return HttpResponse(json.dumps(dict), status=401)

    def post(self,request):
        if request.META["HTTP_OCP_APIM_SUBSCRIPTION_KEY"] == api_key:
            # Preparing Data from Request
            data = list()
            data.append(request.data['Hostel'])
            data.append(request.data['Mode'])
            data.append(request.data['Bank'])
            # Label Encoders load and transform
            encx0 = pickle.load(open('Mess(hr)/Mess(hr)encx0.sav','rb'))
            encx1 = pickle.load(open('Mess(hr)/Mess(hr)encx1.sav','rb'))
            encx2 = pickle.load(open('Mess(hr)/Mess(hr)encx2.sav','rb'))
            d = encx0.transform([data[0]])
            data[0] = d[0]
            d = encx1.transform([data[1]])
            data[1] = d[0]
            d = encx2.transform([data[2]])
            data[2] = d[0]
            # One hot encoder load and transform
            onehenc = pickle.load(open('Mess(hr)/Mess(hr)onehenc.sav','rb'))
            ar = np.array(data)
            ar = ar.reshape(1,-1)
            x_pred=onehenc.transform(ar).toarray()
            k = list()
            for i in range(20):
                if i!=0 and i!=12 and i!=17:
                    k.append(i)
            x_pred = x_pred[:,k]
            # Load Model and Predict
            loaded_model = pickle.load(open('Mess(hr)/Mess(hr)model.sav', 'rb'))
            result = loaded_model.predict(x_pred)
            dict = {'days':result[0]}
            return HttpResponse(json.dumps(dict), status=200)
        else:
            dict = {'message': 'Incorrect API Key'}
            return HttpResponse(json.dumps(dict), status=401)
