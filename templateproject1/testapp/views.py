from django.shortcuts import render
import datetime

# Create your views here.

def template_view(request):
    dt=datetime.datetime.now()
    name='shubham'
    rollno=101
    marks=100
    my_dict={'date':dt,'name':name,'rollno':rollno,'marks':marks}
    return render(request,'testapp/result.html',my_dict)






