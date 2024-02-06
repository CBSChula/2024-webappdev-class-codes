from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hi class!")

def mickey(request):
    return HttpResponse('Hi Mickey')

def smart(request):
    return HttpResponse("Hi Smart..you look very smart!")

def greet(request, name):
    return HttpResponse(f"Hi <h1>{name}</h1>! Hope you learn something new today!")

def attendence_record(request, num_students):
    return HttpResponse(f"There are {num_students} in the class today.")