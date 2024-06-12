from django.shortcuts import render
from django.http import HttpResponse
\



def home(request):
    return HttpResponse("Hello, this is a dynamic web page!")


def home2(request):
    context = {'message': 'Hello, this is a dynamic web page with a template!'}
    return render(request, 'index.html', context)