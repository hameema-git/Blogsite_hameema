# Generated by Django 5.0.6 on 2024-06-24 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_name', models.CharField(max_length=50)),
                ('blog_discription', models.TextField()),
                ('author', models.CharField(max_length=50)),
                ('created_on', models.DateTimeField()),
            ],
        ),
    ]
