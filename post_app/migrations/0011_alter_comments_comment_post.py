# Generated by Django 4.2.5 on 2023-09-14 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0010_remove_post_post_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='post_app.post', verbose_name='Hangi Posta yapıldı'),
        ),
    ]
