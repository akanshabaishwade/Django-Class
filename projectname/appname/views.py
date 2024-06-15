from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import StudentForm



def home(request):
    return HttpResponse("Hello, this is a dynamic web page!")


def home2(request):
    context = {'message': 'Hello, this is a dynamic web page with a template!'}
    return render(request, 'index.html', context)


from .models import Student

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