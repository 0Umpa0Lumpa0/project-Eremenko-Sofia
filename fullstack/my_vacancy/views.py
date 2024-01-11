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


class SkillSet(ListView):
    model = SkillSet
    template_name = 'skillset.html'


class LastVacancy(ListView):
    model = RecentVacancies
    template_name = 'last_vacancy.html'
