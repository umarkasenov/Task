from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('login/', views.AuthorizationView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('greeting/', views.GreetingView.as_view(), name='greeting'),

  ]
