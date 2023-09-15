# Generated by Django 4.2.5 on 2023-09-12 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser_app', '0007_alter_myuser_avatar_alter_myuser_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatar/', verbose_name='Avatar'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='banner/', verbose_name='Banner'),
        ),
    ]