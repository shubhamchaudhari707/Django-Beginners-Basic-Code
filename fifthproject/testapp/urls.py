
from django.urls import path
from testapp import views

urlpatterns = [
    
    path('',views.first_view),
    path('second/',views.second_view),
    path('third/',views.third_view),
    path('fourth/',views.fourth_view),
    path('fifth/',views.fifth_view),
]