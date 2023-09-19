from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm  # Import your custom registration form

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('user_profile')  # Redirect to user profile page or another page after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html',)
