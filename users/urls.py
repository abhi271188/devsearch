from django.urls import path
from . import views

urlpatterns = [
    path('login-register/', views.userLogin, name='login-register'),
    path('logout/', views.userLogout, name='logout'),
    path('', views.Profiles, name='profiles'),
    path('profile/<str:pk>/', views.userProfile, name='profile'),
]