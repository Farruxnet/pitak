# Generated by Django 3.2.3 on 2021-09-01 12:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('drivers', '0005_alter_drivercart_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drivercart',
            name='delivery_user',
            field=models.ManyToManyField(blank=True, null=True, related_name='delivery_user', to=settings.AUTH_USER_MODEL, verbose_name='Pochta'),
        ),
    ]
