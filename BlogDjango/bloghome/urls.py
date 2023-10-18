from django.urls import path
from .views import EditPostView, DeletePostView,AddPostView
from .import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('add_post/',AddPostView.as_view(), name='add-post'),
    path('article/edit/<int:pk>',EditPostView.as_view(), name='update-post'),
    path('article/<int:pk>/remove',DeletePostView.as_view(), name='delete-post'),

]