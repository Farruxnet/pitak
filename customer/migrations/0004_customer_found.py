# Generated by Django 3.2.3 on 2021-09-11 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20210909_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='found',
            field=models.BooleanField(default=False, verbose_name='Qabul qilindi'),
        ),
    ]