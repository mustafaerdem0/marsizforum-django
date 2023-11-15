# Generated by Django 4.2.5 on 2023-09-12 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0005_post_post_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Postun Oluşturulma tarihi'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Postun Oluşturulma tarihi'),
        ),
    ]
