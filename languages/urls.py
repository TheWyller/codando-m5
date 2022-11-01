from django.urls import path
from . import views

urlpatterns = [
    path('languages/', views.LanguageView.as_view()),
    path('languages/<str:language_id>/', views.LanguageDetailView.as_view()),
]
