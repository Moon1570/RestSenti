from django.urls import path
from . import views
  
urlpatterns = [
      #path('sa/', views.sa, name='get-sentiment'),
      path('records/',views.user_records, name='all-records'),
      path('records/<str:pk>',views.records_by_userid, name='records-by-userid'),
      path('new/',views.add_new,name='new'),
]