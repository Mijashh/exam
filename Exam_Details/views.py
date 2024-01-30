from django.shortcuts import render
from django.http import HttpResponse
from .models import ExamIndex,ExamDetails


def exam_view(request):
    exam_items=ExamIndex.objects.all()
    return render(request,"Exam_Details/index.html",{"exam_items":exam_items})

def exam_details_view(request,value):
    exam_details=ExamDetails.objects.all() 
    return render(request,"Exam_Details/details.html",{"exam_details":exam_details})

