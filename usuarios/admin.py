from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from usuarios.models import customUser


class customUserAdmin(UserAdmin):
    model = customUser
    fieldsets = (
        (
            None,
            {"fields": ("username", "email", "password", "first_name", "last_name")},
        ),
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
                    "username",
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )

    list_display = ("username", "email", "is_staff", "is_superuser")
    search_fields = ("username", "email")
    ordering = ("username", "email")


admin.site.register(customUser, customUserAdmin)
