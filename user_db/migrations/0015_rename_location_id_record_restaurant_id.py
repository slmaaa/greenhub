# Generated by Django 3.2.12 on 2022-04-12 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_db', '0014_auto_20220412_2054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='location_id',
            new_name='restaurant_id',
        ),
    ]