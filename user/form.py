from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    email =forms.EmailField()
    phone = forms.CharField(max_length=15)
    address= forms.CharField()
    
    class Meta:
        model = User
        fields=['username', 'email', 'phone', 'password1', 'password2', 'address']