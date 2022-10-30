from django.contrib import admin
from django.urls import path, include
from mailing.urls import router


app_name = 'config'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mailing/', include('mailing.urls'))
]
