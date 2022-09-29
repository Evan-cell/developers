from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import project
from .forms import projectForm
# Create your views here.

def createproject(request):
    form = projectForm()
    if request.method == 'POST':
        form = projectForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('projects')
    context={'form':form}
    return render(request, 'project_form.html', context)
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

