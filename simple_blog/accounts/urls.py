"""simple_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('edit_profile/', views.UserEditView.as_view(), name='edit_profile'),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html'),),
    path('password/', views.PasswordsChangeView.as_view(template_name='registration/change_password.html'),),
    path('password_success/', views.PasswordSuccess.as_view(), name='password_success'),
    path('<int:pk>/profile/', views.ProfilePageView.as_view(), name="view_profile"),
    path('<int:pk>/edit_profile_page/', views.EditProfilePageView.as_view(), name="edit_profile_page"),
    path('create_user_profile/', views.CreateProfilePageView.as_view(), name='create_profile_page')
]
