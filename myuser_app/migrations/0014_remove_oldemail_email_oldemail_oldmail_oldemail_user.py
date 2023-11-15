# Generated by Django 4.2.5 on 2023-10-09 17:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser_app', '0013_oldemail_myuser_oldemail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oldemail',
            name='email',
        ),
        migrations.AddField(
            model_name='oldemail',
            name='oldmail',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='oldemail',
            name='user',
            field=models.ManyToManyField(blank=True, null=True, related_name='oldmailuser', to=settings.AUTH_USER_MODEL, verbose_name='eski mail sahibi'),
        ),
    ]