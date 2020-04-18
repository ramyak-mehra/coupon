# Generated by Django 3.0.5 on 2020-04-18 08:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('coupan', '0007_auto_20200418_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupan',
            name='code',
            field=models.CharField(default='Coupan Code', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coupan',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 19, 8, 42, 51, 109221, tzinfo=utc)),
        ),
    ]
