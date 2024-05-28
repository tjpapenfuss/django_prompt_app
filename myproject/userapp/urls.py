# userapp/urls.py

from django.urls import path
from .views import create_user, get_user_info, get_user_id, get_user_name

urlpatterns = [
    path('create_user/', create_user, name='create_user'),
    path('get_user_info/<str:user_name>/', get_user_info, name='get_user_info'),
    path('get_user_id/<str:user_name>/', get_user_id, name='get_user_id'),
    path('get_user_name/<str:user_id>/', get_user_name, name='get_user_name'),
]
