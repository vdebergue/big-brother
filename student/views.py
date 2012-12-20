from django.http import HttpResponse
from django.template import Template
from django.shortcuts import render

def index(request):
    data = {"title": "Main"}
    return render(request, "main.html", data)
