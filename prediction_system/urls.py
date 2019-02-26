from django.conf.urls import url, include
from . import views

urlpatterns = [
    # Index
    url(r'^$', views.index, name="Index"),
]