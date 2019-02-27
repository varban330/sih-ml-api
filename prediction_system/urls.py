from django.conf.urls import url, include
from . import views

urlpatterns = [
    # Index
    url(r'^$', views.TestView.as_view(), name="Index"),
    url(r'^mess_fee/$', views.MessFeePred.as_view(), name="Mess_Fee"),
    url(r'^scholarship_portal/$', views.SchoPortPred.as_view(), name="Scholarship_Portal"),
]
