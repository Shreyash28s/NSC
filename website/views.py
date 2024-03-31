from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'index.html')

def homepage(request):
    return render(request,"homepage.html")

def boardpage(request):
    return render(request, "boardpage.html")

def events(request):
    return render(request, "events.html")

def membership(request):
    return render(request, "membership.html")

def register(request):
    return render(request, "register.html")

def sponsorship(request):
    return render(request, "sponsorship.html")

def about(request):
    return render(request, "about.html")

