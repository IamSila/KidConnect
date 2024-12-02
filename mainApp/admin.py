from django.contrib import admin
from .models import Analytic, Team, Report

# Register your models here.
admin.site.register(Analytic)
admin.site.register(Team)
admin.site.register(Report)