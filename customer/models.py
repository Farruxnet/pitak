from django.db import models
from users.models import User
from data.models import Province, District, Automobile
from django.utils.timezone import now

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', verbose_name="Foydalanuvchi")
    customer_current_province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='customer_current_province', verbose_name="Turgan viloyat")
    customer_current_district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='customer_current_district', verbose_name="Turgan tuman")
    customer_finish_province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='customer_finish_province', verbose_name="Boradigan viloyat")
    customer_finish_district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='customer_finish_district', verbose_name="Boradigan tuman")
    automobile = models.ForeignKey(Automobile, on_delete=models.CASCADE, verbose_name="Avtomobil")
    passengers_count = models.IntegerField(verbose_name="Yo'lovchi soni")
    phone_number = models.CharField(max_length=12, verbose_name="Telefon raqami")
    date = models.DateTimeField(default=now, verbose_name="Qo'shilgan vaqti")
    latitude = models.CharField(max_length=150, null=True, blank=True, verbose_name='Location latitude')
    longitude = models.CharField(max_length=150, null=True, blank=True, verbose_name='Location longitude')

    SEX = (
        ('man', 'Erkak'),
        ('woman', 'Ayol'),
    )
    
    sex = models.CharField(choices=SEX, max_length=5, verbose_name="Jinsi")
    STATUS = (
        (True, 'Faol'),
        (False, 'Nofaol'),
    )
    status = models.BooleanField(choices=STATUS, default=True, verbose_name="Holati")

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = "Yulovchi e'loni"
        verbose_name_plural = "Yulovchilar e'lonlari"
