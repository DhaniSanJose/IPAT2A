from django.shortcuts import render

# Create your views here.


def home(request):
    #do something

    return render(request, 'home.html')


def register(request):
    
    return render(request, 'register.html')