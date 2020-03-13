from django import forms
from .models import UserProfile
from users.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta:
        model = User
        fields = ['email', 'password']

class UserProfileForm(forms.ModelForm):
     class Meta:
         model = UserProfile
         fields = [
            'first_name',
            'last_name',
            'profile_pic'
         ]
         exclude = ('user',)