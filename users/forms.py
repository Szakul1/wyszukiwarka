from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile



class UserRegisterForm(UserCreationForm):
    """Formularz dla uzytkownika w przyszlej mozliwej implementacji"""
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class UserUpdateForm(forms.ModelForm):
    """Formularz dla uzytkownika w przyszlej mozliwej implementacji"""
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    """Formularz dla profilu w przyszlej mozliwej implementacji"""
    
    class Meta:
        model = Profile
        fields = ['image']