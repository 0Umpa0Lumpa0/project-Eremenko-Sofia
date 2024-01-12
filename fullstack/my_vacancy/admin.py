from django.contrib import admin
from my_vacancy.models import *


@admin.register(MainInfo, JobDemand, CityStatistics, SkillSet, RecentVacancies, Navigations)
class MyModelAdmin(admin.ModelAdmin):
    pass
