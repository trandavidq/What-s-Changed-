from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout as auth_logout

# Create your views here.
def index(request):
    #the default page is the login page
    return render(request,'changed/login.html')



    


def signup(request):
    return render(request,'changed/signup.html')
