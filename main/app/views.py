from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def form_elements(request):
    return render(request, 'form-elements.html')


def form_layout(request):
    a=102

    return render(request, 'form-layout.html')


def hello(request):
    return HttpResponse("Hello, world. You're at the app hello.")


