from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def dhoni(request):
    return HttpResponse('<h1>Dhoni is a MR.. Cool Captain</h1>')

def raina(request):
    return HttpResponse('<marquee><h1>Raina is a CSK Team is More Dangergous Batsman in CSK</marquee></h1>')