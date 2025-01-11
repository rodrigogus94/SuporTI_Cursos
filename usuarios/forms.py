from django import forms
from usuarios.models import customUser


class LoginForms(forms.Form):
    login = forms.EmailField(
        label="Login",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: joaosilva@xpto.com",
            }
        ),
    )
    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite a sua senha",
            }
        ),
    )


class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label="Nome do usuário",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: João Silva",
            }
        ),
    )
    email = forms.EmailField(
        label="Email",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: joaosilva@xpto.com",
            }
        ),
    )
    senha_1 = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite a sua senha",
            }
        ),
    )
    senha_2 = forms.CharField(
        label="Confirme a sua senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite a sua senha novamente",
            }
        ),
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get("nome_cadastro")
        if customUser.objects.filter(nome=nome).exists():
            raise forms.ValidationError("Este usuário já está cadastrado")
        return nome
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if customUser.objects.filter(email = email).exists():
            raise forms.ValidationError("Este e-mail já está cadastrado")
        return email

    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get("senha_1")
        senha_2 = self.cleaned_data.get("senha_2")

        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError("Senhas não são iguais")
            else:
                return senha_2
