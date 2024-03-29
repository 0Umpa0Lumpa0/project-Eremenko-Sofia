from django.contrib import admin
from django.urls import path

from my_vacancy.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('importance', Importance.as_view(), name='importance'),
    path('geography', Geography.as_view(), name='geography'),
    path('skillset', SkillSet.as_view(), name='skillset'),
    path('recent', LastVacancy.as_view(), name='recant_vacs')
]
