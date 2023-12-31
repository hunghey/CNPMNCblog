from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms 



class ChangedPasswordForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100 , widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password1 = forms.CharField(max_length=100 , widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    new_password2 = forms.CharField(max_length=100 , widget=forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
    class Meta:
        model = User
        fields = ('old_password','new_password1','new_password2')