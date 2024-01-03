from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('diary/info/', views.info, name='info'),
    path('diary/', views.PageListView.as_view(), name='page-list'),
    path('diary/write/', views.PageCreateView.as_view(), name='page-create'),
    path('diary/<int:page_id>/', views.PageDetailView.as_view(), name='page-detail'),
    path('diary/page/<int:page_id>/edit/', views.PageUpdateView.as_view(), name='page-update'),
    path('diary/page/<int:page_id>/delete/', views.PageDeleteView.as_view(), name='page-delete'),
]
