from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    #add an entity as a lost child
    path('report/', views.report, name="report"),
    # testing the base.html
    path('base/', views.base, name="base"),
    # listing all reported children
    path('reported/', views.reportedChildren, name="reportedChildren"),
    # the search functionality
    path('search/', views.search, name='search'),
    # a custom admin page
    path('customAdmin/', views.customAdmin, name="customAdmin"),
    # the update button in custom admin
    path('customAdmin/update/<str:id>', views.updateDetails, name="update"),
    # the delete functionality in customAdmin
    path('customAdmin/delete/<str:id>', views.delete, name="delete"),
    # generate a child details as paragraph
    path('generateDetails/<str:id>', views.generateDetails, name="generateDetails")
]
