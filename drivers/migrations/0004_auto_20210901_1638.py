# Generated by Django 3.2.3 on 2021-09-01 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0003_auto_20210901_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='status',
            field=models.BooleanField(choices=[(True, 'Faol'), (False, 'Nofaol')], default=True, verbose_name='Holati'),
        ),
        migrations.AlterField(
            model_name='drivercart',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='drivers.driver', verbose_name='Haydovchi'),
        ),
    ]