from django.shortcuts import render

# Create your views here.
from django.http import  HttpResponse
def jampandu(request):
    return HttpResponse("Hii,Jigelurani")
def jigelurani(request):
    return HttpResponse("Hello,Jampandu")
def ranga(request):
    return HttpResponse("Hello Guys,How are you all")