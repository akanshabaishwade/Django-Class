from django.urls import path
from . import views


# http://127.0.0.1:8000/app/home/

urlpatterns = [
    path('home/', views.home, name='home'),
    path('home2/', views.home2, name='home'),
    
    
]
