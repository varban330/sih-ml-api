from django.conf.urls import url, include
from . import views

urlpatterns = [
    # Index
    url(r'^$', views.Testview.as_view(), name="Index"),
]