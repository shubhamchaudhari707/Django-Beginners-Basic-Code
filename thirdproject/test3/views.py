from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def good_morning_view(request):
    return HttpResponse('hellio friend good morning')

def good_evening_view(request):
    return HttpResponse('hellio friend good evening ')

def good_night_view(request):
    return HttpResponse('hellio friend good night ')
