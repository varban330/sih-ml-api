
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^predict/', include('prediction_system.urls')),
    url(r'^train/', include('training_system.urls'))
]
