from django.urls import path
from . import views
  
urlpatterns = [
      path('sa/', views.sa, name='get-sentiment'),
      path('records/',views.records, name='get-records'),
]