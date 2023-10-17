from django import forms
# from django.forms import ModelForm
import re
# from django.contrib.auth.forms import UserCreationForm
from . models import Post, Category

choices = Category.objects.all().values_list('name','name')

choice_list = []

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','body','snippet')

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            # 'author' : forms.Select(attrs={'class':'form-control'}),
            'body' : forms.Textarea(attrs={'class':'form-control'}),
            'snippet' : forms.Textarea(attrs={'class':'form-control'}),
        }
