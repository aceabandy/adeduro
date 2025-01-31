from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bio/', views.bio, name='bio'),
    path('book/', views.book, name='book'),
    path('contact/', views.contact, name='contact'),
    path('video/', views.video, name='video'),
    
    path('Blog/', views.blog, name='blog'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('search/', views.search, name='search'),
]
