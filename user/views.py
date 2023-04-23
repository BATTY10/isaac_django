from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .form import UserRegistrationForm
from django.contrib import messages
# Create your views here.


def register(request):
    register_form = UserRegistrationForm()
    if request.method == 'POST':
        register_form = UserRegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account created successfully')
            return redirect('/')
        else:
            messages.error(request, 'Account creation failed')
    context = {"register_form": register_form}
    return render(request, 'user/register.html', context)
