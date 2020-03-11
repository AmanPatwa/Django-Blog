from django.contrib import admin
from django.urls import path
from . import views as blog_views
from .views import HomeListView,PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('',HomeListView.as_view(),name = 'blog-home'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('about/',blog_views.about,name = 'blog-about'),
    path('post/new/',PostCreateView.as_view(),name = 'post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name = 'post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name = 'post-delete'),
    path('script/', blog_views.script)
]