# Generated by Django 3.1.6 on 2021-02-15 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='photo',
        ),
        migrations.AddField(
            model_name='news',
            name='category_id',
            field=models.IntegerField(default=1, verbose_name='Категория'),
        ),
    ]