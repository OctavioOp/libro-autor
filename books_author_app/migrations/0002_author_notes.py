# Generated by Django 3.2.5 on 2021-08-09 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_author_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default='a lot notes'),
        ),
    ]
