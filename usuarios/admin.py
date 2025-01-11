from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from usuarios.models import customUser


class customUserAdmin(UserAdmin):
    model = customUser
    fieldsets = (
        (None, {"fields": ("nome", "email", "password", "first_name", "last_name")}),
        (
            "Permissões",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Datas Importantes", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide"),
                "fields": (
                    "nome",
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )

    list_display = ("nome", "email", "is_staff", "is_superuser")
    search_fields = ("nome", "email")
    ordering = ("nome", "email")

admin.site.register(customUser, customUserAdmin)