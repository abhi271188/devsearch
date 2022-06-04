from django.urls import path
from . import views

urlpatterns = [
    path('', views.Profiles, name='profiles'),
    path('profile/<str:pk>/', views.userProfile, name='profile'),
]