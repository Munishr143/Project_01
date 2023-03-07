from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Second_Sample(request):
    return HttpResponse('<h3>Second Sample_func is Executed</h3>')

def first_cmd(request):
    return HttpResponse('Be Confident')

def Second_cmd(request):
    return HttpResponse("Don't waste time")