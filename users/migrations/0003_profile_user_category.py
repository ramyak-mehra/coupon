# Generated by Django 3.0.5 on 2020-04-17 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_category',
            field=models.CharField(default='customer', max_length=100),
            preserve_default=False,
        ),
    ]
