# Generated by Django 2.1.3 on 2018-12-23 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipefyApp', '0005_auto_20181223_1738'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_groceries',
            old_name='starwberry',
            new_name='strawberry',
        ),
    ]
