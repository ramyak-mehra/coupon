# Generated by Django 3.0.5 on 2020-04-18 15:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('coupan', '0013_auto_20200418_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupan',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 19, 15, 13, 19, 795648, tzinfo=utc)),
        ),
    ]
