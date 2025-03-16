from django.urls import path
from .views import (
    postList,
    postDetailView,
    postCreateView,
    postUpdateView,
    postDeleteView
)
from . import views

urlpatterns = [
    path('', postList, name='blog-home'),
    path('post/<int:pk>/', postDetailView, name='post-detail'),
    path('post/new/', postCreateView, name='post-create'),
    path('post/<int:pk>/update/', postUpdateView, name='post-update'),
    path('post/<int:pk>/delete/', postDeleteView, name='post-delete'),
    path('about/', views.about, name='blog-about'),
]
