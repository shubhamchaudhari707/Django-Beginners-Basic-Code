from django.shortcuts import render
from django.http import HttpResponse  
# Create your views here.

def hello_world_view(request):
    return HttpResponse("<h1>Hello this is response from django application</h1>")

def hello_world(request):
    return HttpResponse("<h1>Hello this is shubham</h1>")
    

