from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
    "placeholder": "Entrez un nom d'utilisateur",
    "class": "w-full py-4 px-6 rounded-xl placeholder-teal-600 placeholder-opacity-50",
  }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
    "placeholder": "Votre mot de passe",
    "class": "w-full py-4 px-6 rounded-xl placeholder-teal-600 placeholder-opacity-50",
  }))



class SignupForm(UserCreationForm):
  class Meta:
    model = User
    fields = ("username", "email", "password1", "password2")
  
  username = forms.CharField(widget=forms.TextInput(attrs={
    "placeholder": "Entrez un nom d'utilisateur",
    "class": "w-full py-4 px-6 rounded-xl placeholder-teal-600 placeholder-opacity-50",
  }))
  email = forms.CharField(widget=forms.EmailInput(attrs={
    "placeholder": "exemple@gmail.com",
    "class": "w-full py-4 px-6 rounded-xl placeholder-teal-600 placeholder-opacity-50",
  }))
  password1 = forms.CharField(widget=forms.PasswordInput(attrs={
    "placeholder": "Votre mot de passe",
    "class": "w-full py-4 px-6 rounded-xl placeholder-teal-600 placeholder-opacity-50",
  }))
  password2 = forms.CharField(widget=forms.PasswordInput(attrs={
    "placeholder": "Confirmez votre mot de passe",
    "class": "w-full py-4 px-6 rounded-xl placeholder-teal-600 placeholder-opacity-50",
  }))