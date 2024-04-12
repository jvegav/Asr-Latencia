from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('users/', views.users_list, name ='users_list'),
    path('userCreate/', csrf_exempt(views.user_create),name='userCreate'),
]