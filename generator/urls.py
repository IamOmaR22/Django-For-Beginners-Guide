from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='g-home'),
    path('password/', views.password, name='password'),
]
