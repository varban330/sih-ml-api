from django.conf.urls import url, include
from . import views

urlpatterns = [
    # Index
    url(r'^$', views.TestView.as_view(), name="Index"),
]