# Generated by Django 4.1.7 on 2023-03-06 02:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProfile",
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
                (
                    "org",
                    models.CharField(
                        blank=True, max_length=128, verbose_name="Organization"
                    ),
                ),
                (
                    "tel",
                    models.CharField(
                        blank=True, max_length=50, verbose_name="Telephone"
                    ),
                ),
                (
                    "modify_date",
                    models.DateTimeField(auto_now=True, verbose_name="Last modified"),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "User Profile",
            },
        ),
    ]
