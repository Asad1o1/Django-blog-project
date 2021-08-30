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

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='article_detail'),
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
    path('article/edit_post/<int:pk>/', views.EditPostView.as_view(), name='edit_post'),
    path('article/delete_post/<int:pk>/', views.DeletePostView.as_view(), name='delete_post'),
    path('add_category/', views.AddCategoryView.as_view(), name='add_category'),
    path('category/<str:name>/', views.CategoryView, name='category'),
    path('category_list/', views.CategoryListView, name='category_list'),
    path('like/<int:pk>/', views.LikeView, name='like_post'),
    path('article/<int:pk>/comment', views.AddCommentView.as_view(), name='add_comment'),   
]
