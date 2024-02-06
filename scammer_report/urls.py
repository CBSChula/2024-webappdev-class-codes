from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_list, name='report-list'),
    path('add/', views.add_report, name='add-report'),
]
