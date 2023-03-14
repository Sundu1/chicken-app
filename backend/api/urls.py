from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.usersView, name = 'users' ),
    path('user/<int:pk>', views.userViewByKey, name = 'user-by-key' ),
    path('auth/',views.authentication, name='auth')
]
