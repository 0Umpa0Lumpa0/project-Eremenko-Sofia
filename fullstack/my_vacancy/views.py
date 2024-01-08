from django.shortcuts import render
from django.views.generic import ListView
from my_vacancy.models import MainInfo


class IndexView(ListView):
    model = MainInfo
    template_name = 'index.html'
