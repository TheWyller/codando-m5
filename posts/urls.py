from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostView.as_view()),
    path('posts/<str:post_id>/', views.PostDetailView.as_view()),
]