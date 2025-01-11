from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from datetime import datetime


class customUserManager(BaseUserManager):
    def create_user(self, nome=None, email=None, password=None, **extra_fields):
        if not nome:
            raise ValueError("O nome deve ser fornecido")
        if not email:
            raise ValueError("O endereço de email deve ser fornecido")

        email = self.normalize_email(email)
        user = self.model(nome=nome, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, nome=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superusuário deve ter is_staff igual a True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superusuário deve ter is_superuser igual a True.")

        return self.create_user(nome, email, password, **extra_fields)


class customUser(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(max_length=150, null=False, default="Usuário")
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=datetime.now, blank=False)

    objects = customUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}".strip()
