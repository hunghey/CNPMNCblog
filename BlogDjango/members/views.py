from typing import Any
from django.db import models
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, ChangedPasswordForm, ProfilePageForm
from django.views.generic import DetailView, CreateView
from bloghome.models import Profile
   

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class ChangePasswordView(PasswordChangeView):
    form_class = ChangedPasswordForm
    # form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'registration/password_success.html', {})
    