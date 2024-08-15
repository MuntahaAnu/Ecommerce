from django.urls import path
from .views import *
urlpatterns = [
    path('login/',LOGIN,name = 'login'),
    path('reg/',REG,name = 'reg'),
    path('logout/',LOGOUT,name = 'logout'),
    path('reset/',RESET_PASS,name = 'reset'),
    path('success/',success,name = 'success'),
    path('error/',error,name = 'error'),
    path('token_send /',token_send,name = 'token_send'),
    path('verify/<auth_token>/',verify,name = 'verify'),

]