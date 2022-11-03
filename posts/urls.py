from django.urls import path
from . import views

urlpatterns = [
    path("posts/", views.PostView.as_view()),
    path(
        "posts/me/",
        views.PostsSelfUser.as_view(),
    ),
    path("posts/<str:post_id>/", views.PostDetailView.as_view()),
    path(
        "posts/categories/<str:category_id>/",
        views.PostOnCategoryView.as_view(),
    path(
        "posts/language/<str:language_id>/",
        views.PostOnLanguageView.as_view(),
    ),
]
