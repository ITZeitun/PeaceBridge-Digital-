from django.urls import path
from .views import donate_view

urlpatterns = [
    path('', donate_view, name='donate'),
]
