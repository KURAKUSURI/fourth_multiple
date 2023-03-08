from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def virat(request):
    return HttpResponse('<marquee><h1>Virat is a Best Batsman in the India</marquee></h1>')

def ABD(request):
    return HttpResponse('<h1>ABD is a MR..360 Batsman in a RCB</h1>')
