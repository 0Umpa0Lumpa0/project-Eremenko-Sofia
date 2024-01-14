from django.shortcuts import render
from django.views.generic import View
from my_vacancy.models import *
from my_vacancy.api import HeadHunterParsing


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

    def get_vacs(self):
        recent_vacancy = self.model.objects.first()

        if recent_vacancy:
            search_text = recent_vacancy.content_to_parse

            hh_parser = HeadHunterParsing(search_text=search_text)

            vacancies_data = hh_parser.get_data_vacancies(date='2023-12-20', count_vacancies=10)

            context = {'vacancies_data': vacancies_data, 'context': recent_vacancy.title}
            print(context)
            return context


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

    def get_context_data(self, **kwargs):
        return {'navigation': Navigations.objects.all(), 'vacs': self.get_vacs(), **kwargs}

