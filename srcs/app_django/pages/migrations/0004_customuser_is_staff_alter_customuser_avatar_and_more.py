# Generated by Django 4.2.13 on 2024-07-08 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0003_alter_customuser_is_superuser"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="is_staff",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="avatar",
            field=models.ImageField(blank=True, null=True, upload_to="img_avatars/"),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="password",
            field=models.CharField(max_length=128, verbose_name="password"),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="username",
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
