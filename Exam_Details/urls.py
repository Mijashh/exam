from django.urls import path
from . import views

urlpatterns = [
    path("",views.exam_view,name="index"),
    path("<str:value>/",views.exam_details_view,name="details"),
]
