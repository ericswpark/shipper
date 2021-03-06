from django.urls import path
from django.contrib.auth import views as auth_view

from .views import *

urlpatterns = [
    path('login/', auth_view.LoginView.as_view(), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('password_change/', auth_view.PasswordChangeView.as_view(), name='password_change'),
    path('password_change_done/', auth_view.PasswordChangeDoneView.as_view(), name='password_change_done'),
]
