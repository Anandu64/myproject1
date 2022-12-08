from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def fun1(request):
    return HttpResponse('hello welcome to my')

def fun2(request):
    return render(request,'index.html')