# Generated by Django 3.2.3 on 2021-09-11 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='delivery',
            options={'verbose_name': 'Foydalanuvchi pochtasi', 'verbose_name_plural': 'Foydalanuvchi pochtasi'},
        ),
        migrations.AddField(
            model_name='delivery',
            name='found',
            field=models.BooleanField(default=False, verbose_name='Qabul qilindi'),
        ),
    ]
