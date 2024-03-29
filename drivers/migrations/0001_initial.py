# Generated by Django 3.2.3 on 2021-08-30 07:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number_one', models.CharField(max_length=12)),
                ('phone_number_two', models.CharField(blank=True, max_length=12, null=True)),
                ('cooling_system', models.IntegerField(choices=[(0, "YO'Q"), (1, 'BOR')])),
                ('baggage', models.IntegerField(choices=[(0, "YO'Q"), (1, 'BOR')])),
                ('fuel', models.CharField(choices=[('gaz', 'GAZ'), ('benzin', 'BENZIN')], max_length=6)),
                ('sex', models.CharField(choices=[('man', 'Erkak'), ('woman', 'Ayol')], max_length=5)),
                ('status', models.BooleanField(default=True)),
                ('automobile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.automobile')),
                ('deriction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.deriction')),
                ('district', models.ManyToManyField(to='data.District')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DriverCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empty_count', models.IntegerField()),
                ('delivery', models.BooleanField(default=True)),
                ('current_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='currentlocation', to='data.province')),
                ('customer', models.ManyToManyField(related_name='customer', to=settings.AUTH_USER_MODEL)),
                ('delivery_user', models.ManyToManyField(related_name='delivery_user', to=settings.AUTH_USER_MODEL)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drivers.driver')),
                ('finish_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='finishlocation', to='data.province')),
            ],
        ),
    ]
