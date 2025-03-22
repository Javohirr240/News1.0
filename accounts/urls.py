from django.template.context_processors import request
from django.urls import path, re_path
from .views import user_login, dashboardView, SignUpView, signUpView, user_register, user_edit
from django.contrib.auth.views import (
LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView,
PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView,
)
from django.views.generic import TemplateView
urlpatterns = [
    # path('login/', LoginView.as_view(), name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', dashboardView, name='profile'),
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_change_done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # path('signup/', SignUpView.as_view(), name='signup'),
    # path('signup/', signUpView, name='signup'),
    path('signup/', user_register, name='signup'),
    path('signup_done/', TemplateView.as_view(template_name='accounts/register_done.html'), name='signup_done'),
    path('profile/edit/', user_edit, name='profile_edit'),
]