from django.urls import path, include
from allauth.account.views import LoginView
from django.contrib.auth import views as auth_views

# Create your views here.
url_pattens = [
    path('accounts/login/',
         LoginView.as_view(
             template_name='login.html'),
         name='account_login'),
    path('reset_password/',
         auth_views.PasswordResetView.as_view(
             template_name='forgot-password.html'),
         name='reset_password'),
]