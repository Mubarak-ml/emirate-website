from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from .models import *
from .filters import studentResult
from django.core import serializers
from django.http import Http404


def index(request):
    news = News.objects.all().order_by('-Created')[0:3]
    teachers = Teacher.objects.all()[0:4]
    context = {'news': news, 'teachers':teachers}
    return render(request, 'base/index.html', context)

def about(request):
    return render(request, 'base/about.html')

def admission(request):
   return render(request, 'base/admission.html')

def result(request):
    #if request.method == 'POST':
        #studentID = request.POST.get('StudentNo')
        #term = request.POST.get('TERM')
        #year = request.POST.get('YEAR')
        
        #sresult = Science.objects.raw('select * from Science where StudentNo = "'+studentID+'" and TERM = "'+term+'" and YEAR = "'+year+'"')
        #context = {'sresult': sresult}
    
    return render(request, 'base/result.html')
    
def searchResult(request):
    if request.method == 'POST':
        year = request.POST.get('YEAR')
        term = request.POST.get('TERM')
        studentno = request.POST.get('StudentNo').upper()
        try:
            golds = Science.objects.get(StudentNo=studentno, YEAR=year, TERM=term)
            success = 'Student result retrieved successfully'
        except Science.DoesNotExist:
             return HttpResponse("You have entered Incorrect Student Exam details")
        context = {'gold':golds, 'success':success}
        return render(request, 'base/search_result.html', context)
    else:    
        return render(request, 'base/search_result.html')
    
def searchArts(request):
    if request.method == 'POST':
        year = request.POST.get('YEAR')
        term = request.POST.get('TERM')
        studentno = request.POST.get('StudentNo').upper()
        try:
            gold = Arts.objects.get(StudentNo=studentno, YEAR=year, TERM=term)
            success = 'Student result retrieved successfully'
        except Arts.DoesNotExist:
             return HttpResponse("You have entered Incorrect Student Exam details")
        context = {'gold':gold, 'success':success}
        return render(request, 'base/result_arts.html', context)
    else:    
        return render(request, 'base/result_arts.html')

def searchOne(request):
    if request.method == 'POST':
        year = request.POST.get('YEAR')
        term = request.POST.get('TERM')
        studentno = request.POST.get('StudentNo').upper()
        try:
            gold = Sone.objects.get(StudentNo=studentno, YEAR=year, TERM=term)
            success = 'Student result retrieved successfully'
        except Sone.DoesNotExist:
             return HttpResponse("You have entered Incorrect Student Exam details")
        context = {'gold':gold, 'success':success}
        return render(request, 'base/result_one.html', context)
    else:    
        return render(request, 'base/result_one.html')

def searchJss(request):
    if request.method == 'POST':
        year = request.POST.get('YEAR')
        term = request.POST.get('TERM')
        studentno = request.POST.get('StudentNo').upper()
        try:
            gold = Junior.objects.get(StudentNo=studentno, YEAR=year, TERM=term)
            success = 'Student result retrieved successfully'
        except Junior.DoesNotExist:
             return HttpResponse("You have entered Incorrect Student Exam details")
        context = {'gold':gold, 'success':success}
        return render(request, 'base/result_jss.html', context)
    else:    
        return render(request, 'base/result_jss.html')

def teacher(request):
    staff = Teacher.objects.exclude(department='ADMINISTRATION')
    staff = staff.exclude(department='CLERICAL')
    staff = staff.exclude(department='MANAGEMENT')
    pc = Teacher.objects.get(position='PRINCIPAL')
    admin = Teacher.objects.filter(department='ADMINISTRATION')
    clerical = Teacher.objects.filter(department='CLERICAL')
    context ={'staff':staff, 'pc':pc, 'admin':admin, 'clerical':clerical}
    return render(request, 'base/teacher.html', context)

def news(request):
    news = News.objects.all().order_by('-Created')    
    recent = News.objects.all().order_by('-Created')[0:5]
    #cscience = Science.objects.filter(CLASS='SS 3 GOLD (SCIENCE)').count
    clss = Classe.objects.all()[0:5]
    context = {'news': news, 'recent':recent, 'clss':clss}
    return render(request, 'base/news.html', context)

def single(request, pk):
    single = News.objects.get(id=pk)
    recent = News.objects.all().order_by('-Created')[0:5]
    clss = Classe.objects.all()[0:5]
    context = {'single':single, 'recent':recent, 'clss':clss}
    return render(request, 'base/single.html', context)

def classes(request):
    clss = Classe.objects.all()
    context = {'clss':clss}
    return render(request, 'base/class.html', context)