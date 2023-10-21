from .views import  ChangePasswordView, UserRegisterView
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('password/', ChangePasswordView.as_view(template_name = 'registration/change_password.html')),
    path('password_success', views.password_success, name = 'password_success'),
    path('register/', UserRegisterView.as_view(), name = 'register'),

]