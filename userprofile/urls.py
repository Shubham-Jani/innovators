from re import template
from django.contrib import admin
from django.urls import path, include
from .views import home_view, register_view, login_view, logout_view, profile_view, update_profile_view, activate, about_us_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home_view, name="home"),
    path('accounts/register/', register_view, name='register'),
    path('accounts/login/', login_view, name='login'),
    path('accounts/logout/', logout_view, name='logout'),
    path('accounts/profile/', profile_view, name="profile"),
    path('accounts/profile/update_profile',
         update_profile_view, name="update_profile"),
    path('activate/<uidb64>/<token>', activate, name='activate'),
    path('about_us', about_us_view, name="about_us"),

    # password reset thing
    path('reset_password', auth_views.PasswordResetView.as_view(
        template_name="password_reset.html"), name='reset_password'),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(
        template_name="reset_password_sent.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
        template_name="password_reset_confirm.html"), name="password_reset_confirm"),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(
        template_name="password_reset_complete.html"), name='password_reset_complete'),
]
