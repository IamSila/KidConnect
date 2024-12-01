from django.contrib import admin
from .models import Analytic
from .models import Team

# Register your models here.
admin.site.register(Analytic)
admin.site.register(Team)