from django.urls import path

from . import views

urlpatterns = [
    path("",views.exam_view,name="index"),
    path("<slug:value>/",views.exam_details_view,name="details"),
    path('filter_exams', views.filter_exams, name='filter_exams')
]
