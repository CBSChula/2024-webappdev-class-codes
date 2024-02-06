from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
#    path(*)
#    path("mickey", views.mickey, name="mickey"),
#    path("smart", views.smart, name="smart"),    
    path("<str:name>", views.greet, name="greet"),
    path("<int:num_students>", views.attendence_record, name="attendence_record"),
]