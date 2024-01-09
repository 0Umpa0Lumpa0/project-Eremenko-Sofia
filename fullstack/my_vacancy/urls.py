from django.contrib import admin
from django.urls import path

from my_vacancy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('importance', Importance.as_view(), name='importance')
]
