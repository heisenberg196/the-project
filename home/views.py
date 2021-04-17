from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from allauth.account.views import SignupView, LoginView

# Create your views here.
# def login(request):
#     return render(request, 'home/login.html', {})

# def signup(request):
#     return render(request, 'home/Signup.html', {})



# class MySignupView(SignupView):
#     template_name = 'home/login.html'


# class MyLoginView(LoginView):
#     template_name = 'home/Signup.html'


def index(request):
    return render(request, 'home/index.html', {})
    
def profile(request):
    return render(request, 'home/profile1.html', {})

def resume(request):
    return render(request, 'home/resume.html', {})

def saveResume(request):
    return render(request, 'home/saveResume.html', {})

# def profile2(request):
#     return render(request, 'home/profile2.html', {})

@login_required(login_url="login")
def profile2(request):
    # user_profile = request.user.user_profile
    return render(request, 'home/profile2.html', {})

@login_required(login_url="login")
def editProfile(request):
    return render(request, 'home/editProfile.html', {})

   
    