# Generated by Django 4.1.7 on 2023-04-17 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customers',
            name='image',
        ),
    ]
