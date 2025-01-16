from django.urls import path
from django.contrib.auth import views as auth_views
from usuarios.views import login, cadastro, logout

urlpatterns = [
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('logout', logout, name='logout'),
    
]