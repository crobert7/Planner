from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from meetings.models import Meeting

# Create your views here.

def welcome(request):
    # return HttpResponse("Welcome to the meeting planner!")
    return render(request, "website/welcome.html",
                  {"meetings": Meeting.objects.all()})

def time(request):
    return HttpResponse("This page was served at " + str(datetime.now()))

#about page
def about(request):
    return HttpResponse("Hello my name is Robert")
