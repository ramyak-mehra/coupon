# Generated by Django 3.0.5 on 2020-04-18 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_profile_user_categpry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user_categpry',
            new_name='user_category',
        ),
    ]
