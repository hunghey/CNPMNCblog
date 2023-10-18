from django.shortcuts import render
from .forms import PostForm, EditForm
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from django.urls import reverse_lazy, reverse



class HomeView(ListView):
    model = Post
    template_name = "home.html"
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data()
        context["cat_menu"] = cat_menu
        return context
    
# ---------------Post-----------------------
class AddPostView(CreateView):
    model = Post
    form_class = PostForm 
    template_name = 'add_post.html'

class EditPostView(UpdateView):
    model = Post
    form_class = EditForm 
    template_name = 'update_post.html'
    # fields = ['title','body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

