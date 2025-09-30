from django.shortcuts import render
from django.http import HttpResponse
def p1(request):
    return render (request,'map.html')
def p2(request):
    return render(request,'webpage5.html')
def p3(request):
     return render(request,'webpage1.html')
def p4(request):
     return render(request,'webpage2.html')
def p5(request):
     return render(request,'webpage3.html')
def p6(request):
     return render(request,'webpage4.html')

# Create your views here.
