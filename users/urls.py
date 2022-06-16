from django.urls import path
from . import views

urlpatterns = [
    path('login-register/', views.userLogin, name='login-register'),
    path('logout/', views.userLogout, name='logout'),
    path('register/', views.userRegister, name='register'),
    path('', views.Profiles, name='profiles'),
    path('profile/<str:pk>/', views.userProfile, name='profile'),
    path('account/', views.userAccount, name='account'),
]