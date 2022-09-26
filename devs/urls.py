from django.urls import path
from . import views

urlpatterns = [
     path('devops/', views.developer, name="devs"),
     path('index', views.index, name="index")
]