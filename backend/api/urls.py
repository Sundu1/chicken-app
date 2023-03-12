from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.usersViewByKey, name = 'user-view-key' ),
]
