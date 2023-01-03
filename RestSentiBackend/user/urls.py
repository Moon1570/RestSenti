from django.urls import path
from .views import RegisterAPI
from . import views

urlpatterns = [
    path('', views.user_records, name='all-users'),
    path('all', views.user_records, name='all-users'),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('id/<str:pk>',views.records_by_userid, name='records-by-userid'),

]
