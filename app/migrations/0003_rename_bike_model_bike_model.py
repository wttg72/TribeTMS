# Generated by Django 3.2.5 on 2021-07-26 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_booking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bike',
            old_name='bike_model',
            new_name='model',
        ),
    ]
