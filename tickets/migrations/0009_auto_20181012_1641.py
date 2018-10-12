# Generated by Django 2.1.2 on 2018-10-12 16:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0008_auto_20181011_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 12, 16, 40, 59, 916465, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='last_modified_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 12, 16, 40, 59, 916493, tzinfo=utc)),
        ),
    ]