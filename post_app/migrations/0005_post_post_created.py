# Generated by Django 4.2.5 on 2023-09-12 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0004_post_author_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_created',
            field=models.DateTimeField(auto_now=True, verbose_name='Postun Oluşturulma tarihi'),
        ),
    ]
