# Generated by Django 3.0.5 on 2020-04-18 15:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('coupan', '0012_auto_20200418_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupan',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 19, 15, 9, 22, 706946, tzinfo=utc)),
        ),
    ]
