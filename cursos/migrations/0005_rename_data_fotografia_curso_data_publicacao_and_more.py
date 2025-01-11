# Generated by Django 5.1.4 on 2025-01-11 21:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cursos", "0004_alter_curso_id"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name="curso",
            old_name="data_fotografia",
            new_name="data_publicacao",
        ),
        migrations.RenameField(
            model_name="curso",
            old_name="publicada",
            new_name="publicado",
        ),
        migrations.AddField(
            model_name="curso",
            name="usuario",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="user",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
