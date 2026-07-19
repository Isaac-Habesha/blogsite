
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog_index'),
    path('<int:pk>/', views.detail, name='blog_detail'),
    path('create/', views.create, name='blog_create'),
    path('<int:pk>/edit/', views.edit, name='blog_edit'),
    path('<int:pk>/delete/', views.delete, name='blog_delete'),
]
