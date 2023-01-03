from django.urls import path
from .views import RegisterAPI
from . import views

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),

]
