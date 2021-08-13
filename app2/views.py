from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home2(req):
    return HttpResponse('Hello Welcome to app2 home')

def display2(req):
    return HttpResponse('Hello Welcome to app2 display')