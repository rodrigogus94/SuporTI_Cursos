from django.urls import path
from cursos.views import index, buscar

urlpatterns = [
    path("", index, name="index"),
    path("buscar", buscar, name="buscar"),
   
]
