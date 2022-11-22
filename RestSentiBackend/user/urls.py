from django.urls import path
from . import views

urlpatterns = [
    path('', views.getAllUser, name='user'),
    path('register', views.register, name='register'),
]
