# Generated by Django 2.2.28 on 2023-03-01 13:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SerializerDemo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('age', models.IntegerField(default=0)),
                ('hobby', models.CharField(max_length=255, null=True)),
                ('description', models.TextField(null=True)),
                ('datatime', models.DateTimeField(default=datetime.datetime(2023, 3, 1, 21, 12, 14, 883922))),
            ],
        ),
    ]
