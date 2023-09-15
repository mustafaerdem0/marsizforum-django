# Generated by Django 4.2.5 on 2023-09-12 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser_app', '0003_alter_myuser_avatar_alter_myuser_banner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='about',
            field=models.TextField(blank=True, null=True, verbose_name='Hakkında'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='avatar',
            field=models.ImageField(upload_to='avatar/<function MyUser.user at 0x000001ABD9CAF7E0>', verbose_name='Avatar'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='banner',
            field=models.ImageField(upload_to='banner/<function MyUser.user at 0x000001ABD9CAF7E0>', verbose_name='Banner'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='rank',
            field=models.ManyToManyField(blank=True, null=True, to='myuser_app.rank', verbose_name='Rankı'),
        ),
    ]