# Generated by Django 4.1.6 on 2023-03-23 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_profile_delete_registeruser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile',
            new_name='user',
        ),
    ]
