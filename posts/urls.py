from django.urls import path
from . import views

urlpatterns = [
    path("posts/", views.PostView.as_view()),
    path("posts/filter/", views.ListPostsWithFiltersView.as_view()),
    path("posts/me/", views.PostsSelfUser.as_view()),
    path("posts/<str:post_id>/", views.PostDetailView.as_view()),
    path("posts/categories/<str:category_name>/", views.PostOnCategoryView.as_view()),
    path("posts/language/<str:language_name>/", views.PostOnLanguageView.as_view()),
    path("posts/<str:post_id>/like/", views.AddLike.as_view()),
    path("posts/<str:post_id>/dislike/", views.AddDislike.as_view()),
    path(
        "posts/<str:post_id>/interaction/",
        views.ListPostUserRelationInteraction.as_view(),
    ),
    path("posts/interaction/likes/", views.ListAllLikesInteractions.as_view()),
    path("posts/interaction/dislikes/", views.ListAllDislikesInteractions.as_view()),
]
