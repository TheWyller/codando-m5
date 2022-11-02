from django.urls import path
from . import views

urlpatterns = [
    path('posts/<str:post_id>/comments/', views.CommentView.as_view()),
    path('posts/<str:post_id>/comments/<str:comment_id>', views.CommentDetailView.as_view()),
]
