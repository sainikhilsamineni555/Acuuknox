from django.urls import path
from .views import create_user_view, create_user_rollback_view

urlpatterns = [
    path('create-user/', create_user_view, name='create_user'),
]

urlpatterns = [
    path('create-user/', create_user_view, name='create_user'),
    path('create-user-rollback/', create_user_rollback_view, name='create_user_rollback'),
]
