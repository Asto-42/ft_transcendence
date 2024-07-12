# Generated by Django 4.2.13 on 2024-07-11 16:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GameSession",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("player1", models.CharField(blank=True, max_length=100, null=True)),
                ("player2", models.CharField(blank=True, max_length=100, null=True)),
                ("session_id", models.CharField(max_length=100, unique=True)),
                ("state", models.TextField(default="{}")),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
