from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def greeting_view(request):
    return HttpResponse('Hii shubham how are you?')