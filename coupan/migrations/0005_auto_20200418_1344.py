# Generated by Django 3.0.5 on 2020-04-18 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200418_1314'),
        ('coupan', '0004_delete_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coupan',
            old_name='start_date',
            new_name='publish_date',
        ),
        migrations.AddField(
            model_name='coupan',
            name='users',
            field=models.ManyToManyField(to='users.Profile'),
        ),
    ]
