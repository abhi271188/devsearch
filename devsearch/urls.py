from re import template
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views         # to activate the class based views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include('projects.urls')),
    path('', include('users.urls')),

    # set the urls for Password Reset with the class based views
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)