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


class MessFeePred(APIView):
    def get(self, request):
        if request.META["HTTP_OCP_APIM_SUBSCRIPTION_KEY"] == api_key:
            dict = {'message': 'Mess Fee Prediction'}
            return HttpResponse(json.dumps(dict),status=200)
        else:
            dict = {'message': 'Incorrect API Key'}
            return HttpResponse(json.dumps(dict), status=401)

    def post(self,request):
        try:
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
                dict = {'time1':round(result[0]),
                        'time2':max([1,round(result[0]/1.5)]),
                        'time3':max([1,round(result[0]/2)]),
                        'timeOF':0
                        }
                return HttpResponse(json.dumps(dict), status=200)
            else:
                dict = {'message': 'Incorrect API Key'}
                return HttpResponse(json.dumps(dict), status=401)
        except Exception as e:
            dict = {'message': str(e)}
            return HttpResponse(json.dumps(dict), status=400)


class SchoPortPred(APIView):
    def get(self, request):
        if request.META["HTTP_OCP_APIM_SUBSCRIPTION_KEY"] == api_key:
            dict = {'message': 'Scholarship Portal Prediction'}
            return HttpResponse(json.dumps(dict),status=200)
        else:
            dict = {'message': 'Incorrect API Key'}
            return HttpResponse(json.dumps(dict), status=401)

    def post(self,request):
        try:
            if request.META["HTTP_OCP_APIM_SUBSCRIPTION_KEY"] == api_key:
                # Preparing Data from Request
                data = list()
                data.append(request.data['Area'])
                data.append(request.data['Degree'])
                # Label Encoders load and transform
                encx0 = pickle.load(open('scholarship_portal/scholarship_portalencx0.sav','rb'))
                encx1 = pickle.load(open('scholarship_portal/scholarship_portalencx1.sav','rb'))
                d = encx0.transform([data[0]])
                data[0] = d[0]
                d = encx1.transform([data[1]])
                data[1] = d[0]
                # One hot encoder load and transform
                onehenc = pickle.load(open('scholarship_portal/scholarship_portalonehenc.sav','rb'))
                ar = np.array(data)
                ar = ar.reshape(1,-1)
                x_pred=onehenc.transform(ar).toarray()
                k = list()
                for i in range(6):
                    if i!=0 and i!=3:
                        k.append(i)
                x_pred = x_pred[:,k]
                # Load Model and Predict
                loaded_model = pickle.load(open('scholarship_portal/scholarship_portalmodel.sav', 'rb'))
                result = loaded_model.predict(x_pred)
                dict = {'time1':round(result[0]),
                        'time2':max([1,round(result[0]/1.5)]),
                        'time3':max([1,round(result[0]/2)]),
                        'timeOF':max([1,round(result[0]/2.5)])
                        }
                return HttpResponse(json.dumps(dict), status=200)
            else:
                dict = {'message': 'Incorrect API Key'}
                return HttpResponse(json.dumps(dict), status=401)
        except Exception as e:
            dict = {'message': str(e)}
            return HttpResponse(json.dumps(dict), status=400)


class SchoDisPred(APIView):
    def get(self, request):
        if request.META["HTTP_OCP_APIM_SUBSCRIPTION_KEY"] == api_key:
            dict = {'message': 'Scholarship Disbursement Prediction'}
            return HttpResponse(json.dumps(dict),status=200)
        else:
            dict = {'message': 'Incorrect API Key'}
            return HttpResponse(json.dumps(dict), status=401)

    def post(self,request):
        try:
            if request.META["HTTP_OCP_APIM_SUBSCRIPTION_KEY"] == api_key:
                # Preparing Data from Request
                data = list()
                data.append(request.data['Current_CG'])
                data.append(request.data['Course'])
                data.append(request.data['Category'])
                data.append(request.data['Bank'])
                data.append(request.data['Mode'])
                data.append(request.data['Year'])
                # Label Encoders load and transform
                encx1 = pickle.load(open('scholarship_disbursement/scholarship_disbursementencx1.sav','rb'))
                encx3 = pickle.load(open('scholarship_disbursement/scholarship_disbursementencx3.sav','rb'))
                encx4 = pickle.load(open('scholarship_disbursement/scholarship_disbursementencx4.sav','rb'))
                d = encx1.transform([data[1]])
                data[1] = d[0]
                d = encx3.transform([data[3]])
                data[3] = d[0]
                d = encx4.transform([data[4]])
                data[4] = d[0]
                # One hot encoder load and transform
                onehenc = pickle.load(open('scholarship_disbursement/scholarship_disbursementonehenc.sav','rb'))
                ar = np.array(data)
                ar = ar.reshape(1,-1)
                x_pred=onehenc.transform(ar).toarray()
                k = list()
                notlist = [0,8,12,15,20]
                for i in range(23):
                    if i not in notlist:
                        k.append(i)
                x_pred = x_pred[:,k]
                # Load Model and Predict
                loaded_model = pickle.load(open('scholarship_disbursement/scholarship_disbursementmodel.sav', 'rb'))
                result = loaded_model.predict(x_pred)
                dict = {'time1':round(result[0]),
                        'time2':max([1,round(result[0]/1.5)]),
                        'time3':max([1,round(result[0]/2)]),
                        'timeOF':0
                        }
                return HttpResponse(json.dumps(dict), status=200)
            else:
                dict = {'message': 'Incorrect API Key'}
                return HttpResponse(json.dumps(dict), status=401)
        except Exception as e:
            dict = {'message': str(e)}
            return HttpResponse(json.dumps(dict), status=400)


class WaterSupplyPred(APIView):
    def get(self, request):
        if request.META["HTTP_OCP_APIM_SUBSCRIPTION_KEY"] == api_key:
            dict = {'message': 'Water Supply Prediction'}
            return HttpResponse(json.dumps(dict),status=200)
        else:
            dict = {'message': 'Incorrect API Key'}
            return HttpResponse(json.dumps(dict), status=401)

    def post(self,request):
        try:
            if request.META["HTTP_OCP_APIM_SUBSCRIPTION_KEY"] == api_key:
                # Preparing Data from Request
                data = list()
                data.append(request.data['Issue_with'])
                data.append(request.data['Parts'])
                data.append(request.data['Quantity'])
                data.append(request.data['Availability'])
                data.append(request.data['Need'])

                # Label Encoders load and transform
                encx0 = pickle.load(open('water_supply/watersupplyencx0.sav','rb'))
                encx1 = pickle.load(open('water_supply/watersupplyencx1.sav','rb'))
                encx3 = pickle.load(open('water_supply/watersupplyencx3.sav','rb'))
                encx4 = pickle.load(open('water_supply/watersupplyencx4.sav','rb'))
                d = encx0.transform([data[0]])
                data[0] = d[0]
                d = encx1.transform([data[1]])
                data[1] = d[0]
                d = encx3.transform([data[3]])
                data[3] = d[0]
                d = encx4.transform([data[4]])
                data[4] = d[0]
                # One hot encoder load and transform
                onehenc = pickle.load(open('water_supply/water_supplyonehenc.sav','rb'))
                ar = np.array(data)
                ar = ar.reshape(1,-1)
                x_pred=onehenc.transform(ar).toarray()
                k = list()
                notlist = [0,2,5,7]
                for i in range(10):
                    if i not in notlist:
                        k.append(i)
                x_pred = x_pred[:,k]
                # Load Model and Predict
                loaded_model = pickle.load(open('water_supply/water_supplymodel.sav', 'rb'))
                result = loaded_model.predict(x_pred)
                dict = {'time1':round(result[0]),
                        'time2':max([1,round(result[0]/1.5)]),
                        'time3':max([1,round(result[0]/2)]),
                        'timeOF':max([1,round(result[0]/2.5)])
                        }
                return HttpResponse(json.dumps(dict), status=200)
            else:
                dict = {'message': 'Incorrect API Key'}
                return HttpResponse(json.dumps(dict), status=401)
        except Exception as e:
            dict = {'message': str(e)}
            return HttpResponse(json.dumps(dict), status=400)


class FurniturePred(APIView):
    def get(self, request):
        if request.META["HTTP_OCP_APIM_SUBSCRIPTION_KEY"] == api_key:
            dict = {'message': 'Furniture Prediction'}
            return HttpResponse(json.dumps(dict),status=200)
        else:
            dict = {'message': 'Incorrect API Key'}
            return HttpResponse(json.dumps(dict), status=401)

    def post(self,request):
        try:
            if request.META["HTTP_OCP_APIM_SUBSCRIPTION_KEY"] == api_key:
                # Preparing Data from Request
                data = list()
                data.append(request.data['Parts'])
                data.append(request.data['Quantity'])
                data.append(request.data['Availability'])
                data.append(request.data['Need'])

                # Label Encoders load and transform
                encx0 = pickle.load(open('furniture/furnitureencx0.sav','rb'))
                encx2 = pickle.load(open('furniture/furnitureencx2.sav','rb'))
                encx3 = pickle.load(open('furniture/furnitureencx3.sav','rb'))
                d = encx0.transform([data[0]])
                data[0] = d[0]
                d = encx2.transform([data[2]])
                data[2] = d[0]
                d = encx3.transform([data[3]])
                data[3] = d[0]
                # One hot encoder load and transform
                onehenc = pickle.load(open('furniture/furnitureonehenc.sav','rb'))
                ar = np.array(data)
                ar = ar.reshape(1,-1)
                x_pred=onehenc.transform(ar).toarray()
                k = list()
                notlist = [0,5,7]
                for i in range(10):
                    if i not in notlist:
                        k.append(i)
                x_pred = x_pred[:,k]
                # Load Model and Predict
                loaded_model = pickle.load(open('furniture/furnituremodel.sav', 'rb'))
                result = loaded_model.predict(x_pred)
                dict = {'time1':round(result[0]),
                        'time2':max([1,round(result[0]/1.5)]),
                        'time3':max([1,round(result[0]/2)]),
                        'timeOF':max([1,round(result[0]/2.5)])
                        }
                return HttpResponse(json.dumps(dict), status=200)
            else:
                dict = {'message': 'Incorrect API Key'}
                return HttpResponse(json.dumps(dict), status=401)
        except Exception as e:
            dict = {'message': str(e)}
            return HttpResponse(json.dumps(dict), status=400)


class ElectricityPred(APIView):
    def get(self, request):
        if request.META["HTTP_OCP_APIM_SUBSCRIPTION_KEY"] == api_key:
            dict = {'message': 'Electricty Prediction'}
            return HttpResponse(json.dumps(dict),status=200)
        else:
            dict = {'message': 'Incorrect API Key'}
            return HttpResponse(json.dumps(dict), status=401)

    def post(self,request):
        try:
            if request.META["HTTP_OCP_APIM_SUBSCRIPTION_KEY"] == api_key:
                # Preparing Data from Request
                data = list()
                data.append(request.data['Issue'])
                data.append(request.data['Quantity'])
                data.append(request.data['Availability'])
                data.append(request.data['Need'])

                # Label Encoders load and transform
                encx0 = pickle.load(open('Electricity/Electricityencx0.sav','rb'))
                encx2 = pickle.load(open('Electricity/Electricityencx2.sav','rb'))
                encx3 = pickle.load(open('Electricity/Electricityencx3.sav','rb'))
                d = encx0.transform([data[0]])
                data[0] = d[0]
                d = encx2.transform([data[2]])
                data[2] = d[0]
                d = encx3.transform([data[3]])
                data[3] = d[0]
                # One hot encoder load and transform
                onehenc = pickle.load(open('Electricity/Electricity.sav','rb'))
                ar = np.array(data)
                ar = ar.reshape(1,-1)
                x_pred=onehenc.transform(ar).toarray()
                k = list()
                notlist = [0,2,4]
                for i in range(7):
                    if i not in notlist:
                        k.append(i)
                x_pred = x_pred[:,k]
                # Load Model and Predict
                loaded_model = pickle.load(open('Electricity/Electricitymodel.sav', 'rb'))
                classifier = pickle.load(open('Electricity/ElectricityClassmodel.sav'))
                result = loaded_model.predict(x_pred)
                importance = classifier.predict(x_pred)
                dict = {'time1':round(result[0]),
                        'time2':max([1,round(result[0]/1.5)]),
                        'time3':max([1,round(result[0]/2)]),
                        'timeOF':max([1,round(result[0]/2.5)]),
                        'importance':importance
                        }
                return HttpResponse(json.dumps(dict), status=200)
            else:
                dict = {'message': 'Incorrect API Key'}
                return HttpResponse(json.dumps(dict), status=401)
        except Exception as e:
            dict = {'message': str(e)}
            return HttpResponse(json.dumps(dict), status=400)


class WIFIPred(APIView):
    def get(self, request):
        if request.META["HTTP_OCP_APIM_SUBSCRIPTION_KEY"] == api_key:
            dict = {'message': 'WIFI Prediction'}
            return HttpResponse(json.dumps(dict),status=200)
        else:
            dict = {'message': 'Incorrect API Key'}
            return HttpResponse(json.dumps(dict), status=401)

    def post(self,request):
        try:
            if request.META["HTTP_OCP_APIM_SUBSCRIPTION_KEY"] == api_key:
                # Preparing Data from Request
                data = list()
                data.append(request.data['Issue'])
                data.append(request.data['Area'])
                data.append(request.data['Need'])
                data.append(request.data['Availability'])

                # Label Encoders load and transform
                encx0 = pickle.load(open('WIFI/WIFIencx0.sav','rb'))
                encx1 = pickle.load(open('WIFI/WIFIencx1.sav','rb'))
                encx2 = pickle.load(open('WIFI/WIFIencx2.sav','rb'))
                encx3 = pickle.load(open('WIFI/WIFIencx3.sav','rb'))
                d = encx0.transform([data[0]])
                data[0] = d[0]
                d = encx1.transform([data[1]])
                data[1] = d[0]
                d = encx2.transform([data[2]])
                data[2] = d[0]
                d = encx3.transform([data[3]])
                data[3] = d[0]
                # One hot encoder load and transform
                onehenc = pickle.load(open('WIFI/WIFIonehenc.sav','rb'))
                ar = np.array(data)
                ar = ar.reshape(1,-1)
                x_pred=onehenc.transform(ar).toarray()
                k = list()
                notlist = [0,3,7,9]
                for i in range(11):
                    if i not in notlist:
                        k.append(i)
                x_pred = x_pred[:,k]
                # Load Model and Predict
                loaded_model = pickle.load(open('WIFI/WIFImodel.sav', 'rb'))
                result = loaded_model.predict(x_pred)
                dict = {'time1':round(result[0]),
                        'time2':max([1,round(result[0]/1.5)]),
                        'time3':max([1,round(result[0]/2)]),
                        'timeOF':max([1,round(result[0]/2.5)])
                        }
                return HttpResponse(json.dumps(dict), status=200)
            else:
                dict = {'message': 'Incorrect API Key'}
                return HttpResponse(json.dumps(dict), status=401)
        except Exception as e:
            dict = {'message': str(e)}
            return HttpResponse(json.dumps(dict), status=400)


class RoadsPred(APIView):
    def get(self, request):
        if request.META["HTTP_OCP_APIM_SUBSCRIPTION_KEY"] == api_key:
            dict = {'message': 'Roads Prediction'}
            return HttpResponse(json.dumps(dict),status=200)
        else:
            dict = {'message': 'Incorrect API Key'}
            return HttpResponse(json.dumps(dict), status=401)

    def post(self,request):
        try:
            if request.META["HTTP_OCP_APIM_SUBSCRIPTION_KEY"] == api_key:
                # Preparing Data from Request
                data = list()
                data.append(request.data['Issue'])
                data.append(request.data['Material'])
                data.append(request.data['Availability'])
                data.append(request.data['Manpower'])
                data.append(request.data['Need'])

                # Label Encoders load and transform
                encx0 = pickle.load(open('Roads/Roadsencx0.sav','rb'))
                encx2 = pickle.load(open('Roads/Roadsencx2.sav','rb'))
                encx3 = pickle.load(open('Roads/Roadsencx3.sav','rb'))
                encx4 = pickle.load(open('Roads/Roadsencx4.sav','rb'))
                d = encx0.transform([data[0]])
                data[0] = d[0]
                d = encx2.transform([data[2]])
                data[2] = d[0]
                d = encx3.transform([data[3]])
                data[3] = d[0]
                d = encx4.transform([data[4]])
                data[4] = d[0]
                # One hot encoder load and transform
                onehenc = pickle.load(open('Roads/Roadsonehenc.sav','rb'))
                ar = np.array(data)
                ar = ar.reshape(1,-1)
                x_pred=onehenc.transform(ar).toarray()
                k = list()
                notlist = [0,2,4,6]
                for i in range(9):
                    if i not in notlist:
                        k.append(i)
                x_pred = x_pred[:,k]
                # Load Model and Predict
                loaded_model = pickle.load(open('Roads/Roadsmodel.sav', 'rb'))
                result = loaded_model.predict(x_pred)
                dict = {'time1':round(result[0]),
                        'time2':max([1,round(result[0]/1.5)]),
                        'time3':max([1,round(result[0]/2)]),
                        'timeOF':max([1,round(result[0]/4)])
                        }
                return HttpResponse(json.dumps(dict), status=200)
            else:
                dict = {'message': 'Incorrect API Key'}
                return HttpResponse(json.dumps(dict), status=401)
        except Exception as e:
            dict = {'message': str(e)}
            return HttpResponse(json.dumps(dict), status=400)


class FeesPred(APIView):
    def get(self, request):
        if request.META["HTTP_OCP_APIM_SUBSCRIPTION_KEY"] == api_key:
            dict = {'message': 'Fee Pay Prediction'}
            return HttpResponse(json.dumps(dict),status=200)
        else:
            dict = {'message': 'Incorrect API Key'}
            return HttpResponse(json.dumps(dict), status=401)

    def post(self,request):
        try:
            if request.META["HTTP_OCP_APIM_SUBSCRIPTION_KEY"] == api_key:
                # Preparing Data from Request
                data = list()
                data.append(request.data['Status'])
                data.append(request.data['Mode'])
                data.append(request.data['Bank'])
                # Label Encoders load and transform
                encx0 = pickle.load(open('FeePay/FeePayencx0.sav','rb'))
                encx1 = pickle.load(open('FeePay/FeePayencx1.sav','rb'))
                encx2 = pickle.load(open('FeePay/FeePayencx2.sav','rb'))
                d = encx0.transform([data[0]])
                data[0] = d[0]
                d = encx1.transform([data[1]])
                data[1] = d[0]
                d = encx2.transform([data[2]])
                data[2] = d[0]
                # One hot encoder load and transform
                onehenc = pickle.load(open('FeePay/FeePayonehenc.sav','rb'))
                ar = np.array(data)
                ar = ar.reshape(1,-1)
                x_pred=onehenc.transform(ar).toarray()
                k = list()
                notlist = [0,3,8]
                for i in range(11):
                    if i not in notlist:
                        k.append(i)
                x_pred = x_pred[:,k]
                # Load Model and Predict
                loaded_model = pickle.load(open('FeePay/FeePaymodel.sav', 'rb'))
                result = loaded_model.predict(x_pred)
                dict = {'time1':round(result[0]),
                        'time2':max([1,round(result[0]/1.5)]),
                        'time3':max([1,round(result[0]/2)]),
                        'timeOF':0
                        }
                return HttpResponse(json.dumps(dict), status=200)
            else:
                dict = {'message': 'Incorrect API Key'}
                return HttpResponse(json.dumps(dict), status=401)
        except Exception as e:
            dict = {'message': str(e)}
            return HttpResponse(json.dumps(dict), status=400)


class SportsPred(APIView):
    def get(self, request):
        if request.META["HTTP_OCP_APIM_SUBSCRIPTION_KEY"] == api_key:
            dict = {'message': 'Sports Material Prediction'}
            return HttpResponse(json.dumps(dict),status=200)
        else:
            dict = {'message': 'Incorrect API Key'}
            return HttpResponse(json.dumps(dict), status=401)

    def post(self,request):
        try:
            if request.META["HTTP_OCP_APIM_SUBSCRIPTION_KEY"] == api_key:
                # Preparing Data from Request
                data = list()
                data.append(request.data['Issue'])
                data.append(request.data['Material'])
                data.append(request.data['Availability'])
                data.append(request.data['Manpower'])
                data.append(request.data['Need'])
                # Label Encoders load and transform
                encx0 = pickle.load(open('Sports/Sportsencx0.sav','rb'))
                encx2 = pickle.load(open('Sports/Sportsencx2.sav','rb'))
                encx3 = pickle.load(open('Sports/Sportsencx3.sav','rb'))
                encx4 = pickle.load(open('Sports/Sportsencx4.sav','rb'))
                d = encx0.transform([data[0]])
                data[0] = d[0]
                d = encx2.transform([data[2]])
                data[2] = d[0]
                d = encx3.transform([data[3]])
                data[3] = d[0]
                d = encx4.transform([data[4]])
                data[4] = d[0]
                # One hot encoder load and transform
                onehenc = pickle.load(open('Sports/Sportsonehenc.sav','rb'))
                ar = np.array(data)
                ar = ar.reshape(1,-1)
                x_pred=onehenc.transform(ar).toarray()
                k = list()
                notlist = [0,2,4,6]
                for i in range(9):
                    if i not in notlist:
                        k.append(i)
                x_pred = x_pred[:,k]
                # Load Model and Predict
                loaded_model = pickle.load(open('Sports/Sportsmodel.sav', 'rb'))
                result = loaded_model.predict(x_pred)
                dict = {'time1':round(result[0]),
                        'time2':max([1,round(result[0]/1.5)]),
                        'time3':max([1,round(result[0]/2)]),
                        'timeOF':max([1,round(result[0]/2.5)])
                        }
                return HttpResponse(json.dumps(dict), status=200)
            else:
                dict = {'message': 'Incorrect API Key'}
                return HttpResponse(json.dumps(dict), status=401)
        except Exception as e:
            dict = {'message': str(e)}
            return HttpResponse(json.dumps(dict), status=400)
