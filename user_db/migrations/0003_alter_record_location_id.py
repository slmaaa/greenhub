# Generated by Django 3.2.12 on 2022-04-11 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants_db', '0003_auto_20220410_1857'),
        ('user_db', '0002_alter_record_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='location_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants_db.restaurant'),
        ),
    ]
