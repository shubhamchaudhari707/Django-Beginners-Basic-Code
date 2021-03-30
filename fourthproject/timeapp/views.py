from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def time_view(request):
    time=datetime.datetime.now()
    s='The current date and time now : '+str(time)
    return HttpResponse(s)
