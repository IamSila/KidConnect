from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('report/', views.report, name="report"),
    path('base/', views.base, name="base"),
    path('reported/', views.reportedChildren, name="reportedChildren"),
    path('search/', views.search, name='search'),
]
