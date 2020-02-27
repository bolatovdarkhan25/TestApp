from django.urls import path
from . import views
from rest_framework.authtoken import views as api_auth_views

app_name = 'users'

urlpatterns = [
    path('login/', views.UserLoginAPIView.as_view(), name='login'),
    path('registration/', views.registration_api_view, name='registration')
]