# Generated by Django 4.2.5 on 2023-09-14 19:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post_app', '0007_post_like_post_post_view'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_like', models.PositiveIntegerField(verbose_name='Yorum like')),
                ('comment_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Yorumu yapan kişi')),
                ('comment_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post_app.post', verbose_name='Hangi Posta yapıldı')),
            ],
        ),
    ]