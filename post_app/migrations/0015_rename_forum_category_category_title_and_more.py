# Generated by Django 4.2.5 on 2023-09-16 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0014_alter_post_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='forum_category',
            new_name='category_title',
        ),
        migrations.AddField(
            model_name='category',
            name='category_icon',
            field=models.CharField(default='fasfa', max_length=50, verbose_name='Fontawesome icon only text'),
        ),
    ]
