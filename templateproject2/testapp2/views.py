from django.shortcuts import render
import datetime
# Create your views here.

def template_view(request):
    dt=datetime.datetime.now()
    name='shubham'
    rollno='101'
    my_dict={'date':dt,'name':name,'rollno':rollno}
    return render(request,'testapp2/index.html',my_dict)
