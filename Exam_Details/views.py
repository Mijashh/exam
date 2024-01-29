from django.shortcuts import render


def index(request):
    return render(request,"Exam_Details/index.html")


