from django.shortcuts import render
from django.http import HttpResponse 

def index(request):
    html="Welcome page" + '<a href="/rango/about/">about</a>'
    return HttpResponse(html)

def about(request):
    html = "About section" + '<a href="/rango/">Index</a>'
    return HttpResponse(html)