# Generated by Django 4.1.7 on 2023-04-28 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0019_city_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_property',
            name='city',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='myadmin.city'),
        ),
        migrations.AlterField(
            model_name='post_property',
            name='area',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='myadmin.area'),
        ),
    ]
