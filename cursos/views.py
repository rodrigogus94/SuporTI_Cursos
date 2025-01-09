from django.shortcuts import render
from .models import Curso

def index(request):

    cursos = Curso.objects.all()
    return render(request, "cursos/index.html", {"cursos": cursos})


def imagem(request):
    pass


def buscar(request):
    pass


def login(request):
    pass


def logout(request):
    pass


def cadastro(request):
    pass
