from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from .models import ExamDetails, ExamIndex


def exam_view(request):
    exam_items=ExamIndex.objects.all()
    return render(request,"Exam_Details/index.html",{"exam_items":exam_items})

def exam_details_view(request,value):
    exam_details = ExamDetails.objects.filter(exam_index__slug=value)
    if not exam_details:
        raise Http404
    return render(request, "Exam_Details/details.html", {"exam_details": exam_details})

def filter_exams(request):
    selected_options = request.GET.getlist('options')  
    if not selected_options:
        return HttpResponseRedirect("/exams/")
    
    filtered_exams = ExamDetails.objects.filter(exam_index__university__in=selected_options)
    context = {'filtered_exams': filtered_exams}
    
    
    return render(request, 'Exam_Details/filter.html', context)