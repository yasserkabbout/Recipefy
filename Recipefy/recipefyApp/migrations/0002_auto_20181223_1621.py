# Generated by Django 2.1.3 on 2018-12-23 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipefyApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipes',
            old_name='poulty',
            new_name='poultry',
        ),
        migrations.RenameField(
            model_name='user_preferences',
            old_name='poulty',
            new_name='poultry',
        ),
    ]
