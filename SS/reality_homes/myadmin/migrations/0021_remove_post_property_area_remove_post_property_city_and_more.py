# Generated by Django 4.1.7 on 2023-04-28 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0020_post_property_city_alter_post_property_area'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post_property',
            name='area',
        ),
        migrations.RemoveField(
            model_name='post_property',
            name='city',
        ),
        migrations.RemoveField(
            model_name='post_property',
            name='customers',
        ),
        migrations.DeleteModel(
            name='Add_more_images',
        ),
        migrations.DeleteModel(
            name='Post_property',
        ),
    ]
