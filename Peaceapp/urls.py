from django.urls import path
from .views import donate_view

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Index / Home page
    path('', views.index, name='index'),  # <-- homepage

    # Registration page
    path('register/', views.register_view, name='register'),

    # Login page
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),

    # Logout page
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]