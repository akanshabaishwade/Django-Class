from django.urls import path
from . import views


# http://127.0.0.1:8000/app/home/

urlpatterns = [
    path('home/', views.home, name='home'),
    path('home2/', views.home2, name='home2'), 
    path('students/', views.get_students, name='get_students'),
    path('add_student/', views.add_student, name='add_student'),
    path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),
    path('update_student/<int:pk>/', views.update_student, name='update_student'),


]
