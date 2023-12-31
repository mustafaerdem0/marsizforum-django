# Generated by Django 4.2.5 on 2023-09-12 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser_app', '0002_alter_myuser_options_alter_myuser_about_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='avatar',
            field=models.ImageField(upload_to='avatar/<function MyUser.user at 0x000001CB0610F880>', verbose_name='Avatar'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='banner',
            field=models.ImageField(upload_to='banner/<function MyUser.user at 0x000001CB0610F880>', verbose_name='Banner'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='rank',
            field=models.ManyToManyField(to='myuser_app.rank', verbose_name='Rankı'),
        ),
    ]
