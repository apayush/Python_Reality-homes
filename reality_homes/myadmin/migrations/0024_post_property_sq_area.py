# Generated by Django 4.1.7 on 2023-04-28 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0023_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_property',
            name='sq_area',
            field=models.CharField(default='', max_length=150),
        ),
    ]
