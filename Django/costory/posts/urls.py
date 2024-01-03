from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.IndexRedirectView.as_view(), name='index'),
    # path('posts/', views.post_list, name='post-list'),
    path('posts/', views.PostListView.as_view(), name='post-list'),
    # path('posts/<int:post_id>', views.post_detail, name='post-detail'),
    path('posts/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    # path('posts/new', views.post_create, name='post-create'),
    path('posts/new', views.PostCreateView.as_view(), name='post-create'),
    # path('posts/<int:post_id>/edit', views.post_update, name='post-update'),
    path('posts/<int:pk>/edit', views.PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete', views.PostDeleteView.as_view(), name='post-delete'),
]