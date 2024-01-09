from django.shortcuts import render
from django.views.generic import ListView
from my_vacancy.models import *


class IndexView(ListView):
    model = MainInfo
    template_name = 'index.html'


class Importance(ListView):
    model = JobDemand
    template_name = 'importance.html'


class Geography(ListView):
    model = CityStatistics
    template_name = 'geography.html'
