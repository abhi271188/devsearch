from django.urls import path
from . import views

urlpatterns = [
    path('login-register/', views.userLogin, name='login-register'),
    path('logout/', views.userLogout, name='logout'),
    path('register/', views.userRegister, name='register'),
    path('', views.Profiles, name='profiles'),
    path('profile/<str:pk>/', views.userProfile, name='profile'),
    path('account/', views.userAccount, name='account'),
    path('update-profile/', views.updateProfile, name='update-profile'),
    path('add-skill/', views.addSkill, name='add-skill'),
    path('update-skill/<str:pk>/', views.updateSkill, name='update-skill'),
    path('delete-skill/<str:pk>', views.deleteSkill, name='delete-skill'),
    path('inbox/', views.userInbox, name='user-inbox'),
    path('message/<str:pk>/', views.userMessage, name='message'),
]