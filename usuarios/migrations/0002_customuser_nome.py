# Generated by Django 5.1.4 on 2025-01-11 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usuarios", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="nome",
            field=models.CharField(default="Usuário", max_length=150),
        ),
    ]
