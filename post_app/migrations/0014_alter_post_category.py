# Generated by Django 4.2.5 on 2023-09-16 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0013_alter_comments_comment_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='postcategory', to='post_app.category', verbose_name='Kategorini Seç'),
        ),
    ]
