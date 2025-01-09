from django.contrib import admin
from django.urls import path
from cursos.views import index, imagem, buscar, login, cadastro, logout

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("buscar", buscar, name="buscar"),
    path("login", login, name="login"),
    path("cadastro", cadastro, name="cadastro"),
    path("logout", logout, name="logout"),
]
