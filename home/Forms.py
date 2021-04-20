from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db.models import fields
from django.forms import ModelForm

from .models import Profile, Skill

class EditProfileForm(ModelForm):
    class Meta:
        model = User
        fields = (
                 'email',
                 'first_name',
                 'last_name'
                )
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('city',  'phone', 'image') #Note that we didn't mention user field here.

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'