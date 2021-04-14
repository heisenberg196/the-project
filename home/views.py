from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'home/login.html', {})

def signup(request):
    return render(request, 'home/Signup.html', {})

def index(request):
    return render(request, 'home/index.html', {})