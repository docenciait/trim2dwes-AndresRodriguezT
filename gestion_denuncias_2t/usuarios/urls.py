from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='usuarios.signup'),
    path('login/', views.login, name='usuarios.login'),
    path('logout/', views.logout, name='usuarios.logout')
]
