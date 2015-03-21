from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

@login_required(login_url='/login')
def index(request):
    return HttpResponse("You are logged in")

@login_required(login_url='/login')
def home(request):
    return HttpResponse("<h1>HEADER</h1>");


