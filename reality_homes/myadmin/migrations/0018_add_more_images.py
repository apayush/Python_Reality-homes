# Generated by Django 4.1.7 on 2023-04-27 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0017_delete_add_more_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_more_images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=255)),
                ('post_property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.post_property')),
            ],
            options={
                'db_table': 'add_more_images',
            },
        ),
    ]
