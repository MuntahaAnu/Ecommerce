from django.urls import path
from .views import *
urlpatterns = [
    path('login/',LOGIN,name = 'login'),
    path('reg/',REG,name = 'reg'),
    path('logout/',LOGOUT,name = 'logout'),
]