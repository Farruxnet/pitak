# Generated by Django 3.2.3 on 2021-08-26 14:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SmsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=12)),
                ('code', models.IntegerField(default='182182')),
                ('create_at', models.DateTimeField(default=datetime.datetime(2021, 8, 26, 14, 52, 56, 432529))),
            ],
        ),
    ]
