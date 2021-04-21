from home.models import Skill
from django.shortcuts import render, redirect
from datetime import datetime
from .Forms import (EditProfileForm, ProfileForm, SkillForm)
from django.contrib.auth import update_session_auth_hash
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

def showList(request):
    return render(request, 'project/list.html', {})    

# def profile2(request):
#     return render(request, 'home/profile2.html', {})
@login_required(login_url="login")
def editProfile(request):
    if request.method == 'POST':
        
        form = EditProfileForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)  # request.FILES is show the selected image or file
        skill_form = SkillForm(request.POST, instance=request.user)
        # print(skill_form.cleaned_data['rating'], skill_form.cleaned_data['name'])
        # print(request.POST.get('name', ''), request.POST.get('rating', ''))
        if request.method == 'POST':
            skill_form = SkillForm(request.POST)
        if form.is_valid():
            skill, created = Skill.objects.get_or_create(**skill_form.cleaned_data)

        # print(request.POST.get('npc_skills', ''), form, profile_form, skill_form)
        if form.is_valid() and profile_form.is_valid():
            user_form = form.save()
            custom_form = profile_form.save(False)
            custom_form.user = user_form
            custom_form.save()
            return redirect('profile2')
    else:
        form = EditProfileForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        skill_form = SkillForm(instance=request.user)

        args = {}
        # args.update(csrf(request))
        args['form'] = form
        args['profile_form'] = profile_form
        args['skill_form'] = skill_form
        return render(request, 'home/editProfile.html', args)


@login_required(login_url="login")
def profile2(request):
    # user_profile = request.user.user_profile
    return render(request, 'home/profile2.html', {})

# @login_required(login_url="login")
# def editProfile(request):
#     return render(request, 'home/editProfile.html', {})

   
    