from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta: #standard format
        model = Tweet
        fields = ['text', 'photo'] #these text and photos are from models.py
        
        
        
class UserRegistrationForm(UserCreationForm):
   email =  forms.EmailField(required=False)
   class Meta:
       model = User
       fields = ('username', 'email', 'password1', 'password2')
       

            