from django.urls import path
from .views import dashboardView, SignUpView
from django.contrib.auth.views import (
LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView,
PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView,
)
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', dashboardView, name='profile'),
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_change_done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('signup/', SignUpView.as_view(), name='signup'),
]