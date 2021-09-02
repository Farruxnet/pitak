from django.db import models
from users.models import User
from data.models import Deriction, Province, District, Automobile
from django.utils.timezone import now

class Driver(models.Model):
    BAGGAGE = (
        (0, 'YO\'Q'),
        (1, 'BOR'),
    )

    COOLING = (
        (0, 'YO\'Q'),
        (1, 'BOR'),
    )

    FUEL = (
        ('gaz', 'GAZ'),
        ('benzin', 'BENZIN'),
    )

    SEX = (
        ('man', 'Erkak'),
        ('woman', 'Ayol'),
    )

    STATUS = (
        (True, 'Faol'),
        (False, 'Nofaol'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Foydalanuvchi")
    deriction = models.ForeignKey(Deriction, on_delete=models.CASCADE, verbose_name="Yo'nalish")
    district = models.ManyToManyField(District, verbose_name="Qatnov tumanlari")
    automobile = models.ForeignKey(Automobile, on_delete=models.CASCADE, verbose_name="Avtomobil rusumi")
    phone_number_one = models.CharField(max_length=12, verbose_name="Telefon raqam")
    phone_number_two = models.CharField(max_length=12, null=True, blank=True, verbose_name="Qo'shimcha telefon raqam")
    cooling_system = models.IntegerField(choices=COOLING, verbose_name="Sovutish tizimi")
    baggage = models.IntegerField(choices=BAGGAGE, verbose_name="Yuk")
    fuel = models.CharField(choices=FUEL, max_length=6, verbose_name="Yoqilg'i turi")
    sex = models.CharField(choices=SEX, max_length=5, verbose_name="Jinsi")
    create_at = models.DateTimeField(default=now)
    status = models.BooleanField(choices=STATUS, default=True, verbose_name="Holati")

    class Meta:
        verbose_name = "Haydovchi"
        verbose_name_plural = "Haydovchi e'loni"

class DriverCart(models.Model):
    STATUS = (
        (True, 'Faol'),
        (False, 'Nofaol'),
    )
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, verbose_name="Haydovchi", null=True, blank=True)
    customer = models.ManyToManyField(User, related_name='customer', verbose_name="Yulovchi", null=True, blank=True)
    delivery_user = models.ManyToManyField(User, related_name='delivery_user', verbose_name="Olingan pochta egasi", null=True, blank=True)
    current_location = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='currentlocation', verbose_name="Hozirgi manzil")
    finish_location = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='finishlocation', verbose_name="Boradigan manzil")
    empty_count = models.IntegerField(verbose_name="Bo'sh joylar soni")
    delivery = models.BooleanField(default=True, verbose_name="Pochta")
    create_at = models.DateTimeField(default=now)
    status = models.BooleanField(choices=STATUS, default=True, verbose_name="Holati")

    def __str__(self):
        return str(self.driver)

    class Meta:
        verbose_name = "Qidiruv"
        verbose_name_plural = "Qidiruv e'loni"











#