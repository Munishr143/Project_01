from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Sample_1(request):
    return HttpResponse('<h1>Sample function_1 is Executed</h1>')

def Cmd_1(request):
    return HttpResponse('Regularly will attend the class.')

def Cmd_2(request):
    return HttpResponse('Practice Regularly')