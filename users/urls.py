from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('login/', obtain_auth_token),
    path('users/', views.UserView.as_view()),
    path('users/<str:user_id>/', views.UserDetailView.as_view()),
]
