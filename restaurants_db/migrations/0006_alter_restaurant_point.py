# Generated by Django 3.2.12 on 2022-04-13 17:21

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants_db', '0005_alter_restaurant_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='point',
            field=django.contrib.gis.db.models.fields.PointField(editable=False, null=True, srid=2326),
        ),
    ]
