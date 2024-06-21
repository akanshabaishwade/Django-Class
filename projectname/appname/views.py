from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import StudentForm
from .models import Student
# from appname.models import *



def home(request):
    return HttpResponse("Hello, this is a dynamic web page!")


def home2(request):
    context = {'message': 'Hello, this is a dynamic web page with a template!'}
    return render(request, 'index.html', context)



def get_students(request):
    students = Student.objects.all()
    return render(request, 'students3.html', {'students': students})


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_students')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})


def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('get_students')
    return render(request, 'confirm_delete.html', {'student': student})



def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('get_students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'update_student.html', {'form': form})