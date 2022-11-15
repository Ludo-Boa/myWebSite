from django.shortcuts import render

from django.http import HttpResponse

# def home(request):
#     return render(request,'hello/hello.html')


def home(request):
    return render(request, "hello/home.html")

def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")

