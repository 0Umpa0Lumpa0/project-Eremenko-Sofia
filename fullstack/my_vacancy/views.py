from django.shortcuts import render
from django.views.generic import View
from my_vacancy.models import *


class BasePageView(View):
    template_name = None
    model = None
    context_name = None

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        return {'navigation': Navigations.objects.all(), 'context': self.get_queryset(), **kwargs}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())


class IndexView(BasePageView):
    model = MainInfo
    template_name = 'index.html'


class Importance(BasePageView):
    model = JobDemand
    template_name = 'importance.html'


class Geography(BasePageView):
    model = CityStatistics
    template_name = 'geography.html'


class SkillSet(BasePageView):
    model = SkillSet
    template_name = 'skillset.html'


class LastVacancy(BasePageView):
    model = RecentVacancies
    template_name = 'last_vacancy.html'
