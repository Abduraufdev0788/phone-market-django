from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def home(requests:HttpRequest):
    return render(request=requests, template_name="index.html")
