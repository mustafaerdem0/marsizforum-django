# Generated by Django 4.2.5 on 2023-09-19 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myuser_app', '0009_myuser_favorites'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='favorites',
        ),
    ]
