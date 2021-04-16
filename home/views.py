from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'home/login.html', {})

def signup(request):
    return render(request, 'home/Signup.html', {})

def index(request):
    return render(request, 'home/index.html', {})
    
def profile(request):
    return render(request, 'home/profile1.html', {})
# kyaa baat hai django sikh gya ladke
def profile2(request):
    return render(request, 'home/profile2.html', {})

    # /profile m ja kr dekh  
    