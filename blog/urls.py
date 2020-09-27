from django.urls import path
from .views import  PostUpdateView, PostDeleteView, PostCreateView
from . import views

urlpatterns = [
    #path('', PostListView.as_view(), name='blog-home'),
    path('', views.home, name='blog-home'),
    #path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/', views.PostDetailASJSON, name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    #path('post/new/', views.post_new, name='post-create'),
    path('post/new', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]
