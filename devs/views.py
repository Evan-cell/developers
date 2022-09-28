from django.shortcuts import render
from django.http import HttpResponse
from .models import project
# Create your views here.
def developer(request):
    context={}
    return HttpResponse('i code everyday')
def index(request):
    projects = project.objects.all()
    context = {'projects': projects}
    return render(request, 'index.html', context) 
def projects(request, pk):
    projectobj = project.objects.get(id=pk)
    context = {'projectobj':projectobj}
    return render(request, 'single_project.html', context)    

