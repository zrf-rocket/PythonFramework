# Generated by Django 4.2.2 on 2023-07-03 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="pdf_list",
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
                ("is_pdf", models.JSONField(null=True, verbose_name="是否是PDF文件")),
            ],
        ),
    ]