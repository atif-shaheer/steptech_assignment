from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('users/', views.users_table, name='users_table'),
    path('users/<int:user_id>/', views.user_details, name='user_details'),
]
