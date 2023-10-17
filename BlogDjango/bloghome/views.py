from django.shortcuts import render
from .forms import EditForm
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy, reverse


# ---------------Post-----------------------
class EditPostView(UpdateView):
    model = Post
    form_class = EditForm 
    template_name = 'update_post.html'
    # fields = ['title','body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

