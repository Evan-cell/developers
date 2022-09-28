from pickle import TRUE
from pydoc import describe
from tkinter import CASCADE
from turtle import title
from django.db import models
import uuid
# Create your models here.
class project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)
    demo_link = models.CharField(max_length=2000,null=True,blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, blank=True,null=True)
    vote_ratio = models.IntegerField(default=0, blank=True,null=True)
    source_link = models.CharField(max_length=2000,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title 
class review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    project = models.ForeignKey(project, on_delete=models.CASCADE)
    body = models.CharField(max_length=200, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.value
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False) 

    def __str__(self):
        return self.name
