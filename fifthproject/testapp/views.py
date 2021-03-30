from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def first_view(request):
    return HttpResponse('<h1>Response from first value </h1>')

def second_view(request):
    return HttpResponse('<h1>Response from second value </h1>')

def third_view(request):
    return HttpResponse('<h1>Response from third value </h1>')

def fourth_view(request):
    return HttpResponse('<h1>Response from fourth value </h1>')

def fifth_view(request):
    return HttpResponse('<h1>Response from fifth value </h1>')