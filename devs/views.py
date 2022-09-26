from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def developer(request):
    context={}
    return HttpResponse('i code everyday')
def index(request):
    return render(request, 'index.html')    