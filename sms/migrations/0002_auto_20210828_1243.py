# Generated by Django 3.2.3 on 2021-08-28 12:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smsmodel',
            name='code',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='smsmodel',
            name='create_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
