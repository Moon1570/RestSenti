from django.urls import path
from .views import RegisterAPI, LoginAPI
from . import views
from knox import views as knox_views

urlpatterns = [
    path('', views.user_records, name='all-users'),
    path('all', views.user_records, name='all-users'),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('id/<str:pk>',views.records_by_userid, name='records-by-userid'),
    
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
