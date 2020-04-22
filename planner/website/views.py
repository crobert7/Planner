from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def welcome(response):
    return HttpResponse("Welcome to the meeting planner!")

def time(request):
    return HttpResponse("This page was served at " + str(datetime.now()))

#about page
def about(request):
    return HttpResponse("Hello my name is Robert")
