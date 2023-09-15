# Generated by Django 4.2.5 on 2023-09-12 11:20

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0002_post_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True),
        ),
    ]
