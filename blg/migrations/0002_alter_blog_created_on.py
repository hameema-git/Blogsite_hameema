# Generated by Django 5.0.6 on 2024-06-24 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blg', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
