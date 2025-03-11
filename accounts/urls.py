from django.urls import path, re_path
from .views import user_login, dashboardView
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('profile/', dashboardView, name='profile'),
]