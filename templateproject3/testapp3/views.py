from django.shortcuts import render

# Create your views here.
def tempalte_view(request):
    return render(request,'testapp3/index.html')