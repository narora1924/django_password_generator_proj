from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html', {'password':'dsfsdgdfgdfg'})

def veggies(request):
    return HttpResponse("How awsome veggies are")

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxz')

    if request.GET.get('uppercase'):
       characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ') 

    if request.GET.get('special'):
       characters.extend('!@#$%^^&&&*') 

    if request.GET.get('numbers'):
       characters.extend('1234567890') 

    length = int(request.GET.get('length',14))

    thepassword=''

    for x in range(length):
        thepassword += random.choice(characters)


    return render(request, 'generator/password.html', {'password':thepassword})

def about(request):
    return render(request, 'generator/about.html')