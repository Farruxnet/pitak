from django.db import models

class Province(models.Model):
    oz = models.CharField(max_length=50, unique=True, verbose_name="O'zbek")
    uz = models.CharField(max_length=50, unique=True, verbose_name="Узбек")
    ru = models.CharField(max_length=50, unique=True, verbose_name="Rus")
    en = models.CharField(max_length=50, unique=True, verbose_name="English")

    def __str__(self):
        return self.oz

    class Meta:
        verbose_name = "Viloyat"
        verbose_name_plural = "Viloyatlar"

class District(models.Model):
    oz = models.CharField(max_length=50, unique=True, verbose_name="O'zbek")
    uz = models.CharField(max_length=50, unique=True, verbose_name="Узбек")
    ru = models.CharField(max_length=50, unique=True, verbose_name="Rus")
    en = models.CharField(max_length=50, unique=True, verbose_name="English")
    province = models.ForeignKey(Province, on_delete=models.CASCADE, verbose_name='Tegishli viloyat')

    def __str__(self):
        return self.oz

    class Meta:
        verbose_name = "Tuman"
        verbose_name_plural = "Tumanlar"

class Automobile(models.Model):
    AUTO_CATEGORY = (
        ('1', '1-TOIFA'),
        ('2', '2-TOIFA'),
        ('3', '3-TOIFA'),
        ('4', '4-TOIFA'),
    )
    oz = models.CharField(max_length=50, unique=True, verbose_name="O'zbek")
    uz = models.CharField(max_length=50, unique=True, verbose_name="Узбек")
    ru = models.CharField(max_length=50, unique=True, verbose_name="Rus")
    en = models.CharField(max_length=50, unique=True, verbose_name="English")
    category = models.CharField(choices=AUTO_CATEGORY, max_length=2, verbose_name='Kategorya')

    def __str__(self):
        return self.oz

    class Meta:
        verbose_name = "Avtomobil"
        verbose_name_plural = "Avtomobillar"

class Deriction(models.Model):
    a_deriction = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='aderiction', verbose_name="A manzil")
    b_deriction = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='bderiction', verbose_name="B manzil")
    c_deriction = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='cderiction', verbose_name="C manzil")

    def __str__(self):
        return f'{self.a_deriction}-{self.b_deriction}-{self.c_deriction}'

    class Meta:
        verbose_name = "Yo'nalish"
        verbose_name_plural = "Yo'nalishlar"
