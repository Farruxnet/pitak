# Generated by Django 3.2.3 on 2021-09-18 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0009_auto_20210911_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='comment',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Izoh'),
        ),
    ]
