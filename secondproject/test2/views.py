from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def date_time_view(request):
    date=datetime.datetime.now()
    s='the current date and time at server is : '+str(date)
    return HttpResponse(s)