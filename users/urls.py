from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('login/', obtain_auth_token),
    path('users/', views.____.as_view()),
    path('users/<str:user>/', views.____.as_view()),
]
