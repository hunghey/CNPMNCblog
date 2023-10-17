from django.urls import path
from .views import EditPostView, DeletePostView
from django.contrib.auth import views as auth_views
urlpatterns = [

    path('article/edit/<int:pk>',EditPostView.as_view(), name='update-post'),
    path('article/<int:pk>/remove',DeletePostView.as_view(), name='delete-post'),

]