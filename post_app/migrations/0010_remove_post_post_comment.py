# Generated by Django 4.2.5 on 2023-09-14 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0009_post_post_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_comment',
        ),
    ]
