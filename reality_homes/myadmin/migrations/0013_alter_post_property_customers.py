# Generated by Django 4.1.7 on 2023-04-26 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0012_rename_customers_post_property_customers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_property',
            name='customers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.customers'),
        ),
    ]
