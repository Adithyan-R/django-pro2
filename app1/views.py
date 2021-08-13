from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home1(req):
    return HttpResponse('Hello Welcome to app1 home')

def display1(req):
    return HttpResponse('Hello Welcome to app1 display')