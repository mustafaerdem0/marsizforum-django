# Generated by Django 4.2.5 on 2023-09-14 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0008_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='post_app.comments', verbose_name='Posta ait yorumlar'),
        ),
    ]
