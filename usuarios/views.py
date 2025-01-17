from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from usuarios.models import customUser
from django.contrib import messages


def login(request):
    form = LoginForms()

    if request.method == "POST":
        form = LoginForms(request.POST)

        if form.is_valid():
            email = form["login"].value()
            senha = form["senha"].value()

        usuario = authenticate(request, email=email, password=senha)
        if usuario is not None:
            auth_login(request, usuario)
            messages.success(request, f"{request.user.username} logado com sucesso!")
            return redirect("index")
        else:
            messages.error(request, "Erro ao efetuar login")
            return redirect("login")

    return render(request, "cursos/usuarios/login.html", {"form": form})


def cadastro(request):
    form = CadastroForms()

    if request.method == "POST":
        form = CadastroForms(request.POST)

        if form.is_valid():
            nome = form["nome_cadastro"].value()
            email = form["email"].value()
            senha = form["senha_1"].value()

            if customUser.objects.filter(username=nome).exists():
                messages.error(request, "Usuário já existente")
                return redirect("cadastro")

            if customUser.objects.filter(email=email).exists():
                messages.error(request, "E-mail já cadastrado.")
                return redirect("cadastro")

            usuario = customUser.objects.create_user(
                username=nome, email=email, password=senha
            )
            usuario.save()
            messages.success(request, "Cadastro efetuado com sucesso!")
            return redirect("login")

    return render(request, "cursos/usuarios/cadastro.html", {"form": form})


def logout(request):
    auth_logout(request)
    messages.success(request, "Logout efetuado com sucesso!")
    return redirect("login")
