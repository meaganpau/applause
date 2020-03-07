from django import forms
from .models import UserProfile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

class UserProfileForm(forms.ModelForm):
     class Meta:
         model = UserProfile
         fields = [
            'profile_pic'
         ]

class UserUpdateForm(forms.ModelForm):
     class Meta:
         model = User
         fields = [
            'first_name',
            'last_name',
            'email'
         ]