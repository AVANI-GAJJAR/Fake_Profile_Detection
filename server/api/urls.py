from django.urls import path
from . import views

urlpatterns = [
  
    path('api/signup/',views.signup),
    path('api/login/',views.login),
  
]
