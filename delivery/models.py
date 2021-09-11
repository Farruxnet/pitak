from django.db import models
from users.models import User
from data.models import *
from drivers.models import *

class Delivery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_current_location = models.ForeignKey(Province, on_delete=models.CASCADE, related_name = 'deliverycurrentlocation')
    delivery_current_district = models.ForeignKey(District, on_delete=models.CASCADE, related_name = 'deliverycurrentdistrict')
    delivery_finish_location = models.ForeignKey(Province, on_delete=models.CASCADE, related_name = 'deliveryfinishlocation')
    delivery_finish_district = models.ForeignKey(District, on_delete=models.CASCADE, related_name = 'deliveryfinishdistrict')
    delivery_type = models.ForeignKey(DeliveryType, on_delete=models.CASCADE)
    found = models.BooleanField(default=False, verbose_name='Qabul qilindi')
    latitude = models.CharField(max_length=150, null=True, blank=True, verbose_name='Location latitude')
    longitude = models.CharField(max_length=150, null=True, blank=True, verbose_name='Location longitude')
    STATUS = (
        (True, 'Faol'),
        (False, 'Nofaol'),
    )
    status = models.BooleanField(choices=STATUS, default=True, verbose_name="Holati")

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = "Foydalanuvchi pochtasi"
        verbose_name_plural = "Foydalanuvchi pochtasi"
