from django.conf.urls import url, include
from . import views

urlpatterns = [
    # Index
    url(r'^$', views.TestView.as_view(), name="Index"),
    url(r'^mess_fee/$', views.MessFeePred.as_view(), name="Mess_Fee"),
    url(r'^scholarship_portal/$', views.SchoPortPred.as_view(), name="Scholarship_Portal"),
    url(r'^scholarship_disbursement/$', views.SchoDisPred.as_view(), name="Scholarship_Disbursement"),
    url(r'^water_supply/$', views.WaterSupplyPred.as_view(), name="Water_Supply"),
    url(r'^furniture/$', views.FurniturePred.as_view(), name="Furniture"),
    url(r'^electricity/$', views.ElectricityPred.as_view(), name="Electricity"),
    url(r'^wifi/$', views.WIFIPred.as_view(), name="WIFI"),
    url(r'^roads/$', views.RoadsPred.as_view(), name="Roads"),
    url(r'^feepay/$', views.FeesPred.as_view(), name="Fees"),
    url(r'^sports/$', views.SportsPred.as_view(), name="Sports"),
]
