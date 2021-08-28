from django.db import models

class Province(models.Model):
    oz = models.CharField(max_length=50, unique=True)
    uz = models.CharField(max_length=50, unique=True)
    ru = models.CharField(max_length=50, unique=True)
    en = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.oz

class District(models.Model):
    oz = models.CharField(max_length=50, unique=True)
    uz = models.CharField(max_length=50, unique=True)
    ru = models.CharField(max_length=50, unique=True)
    en = models.CharField(max_length=50, unique=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self):
        return self.oz

class Automobile(models.Model):
    AUTO_CATEGORY = (
        ('1', '1-TOIFA'),
        ('2', '2-TOIFA'),
        ('3', '3-TOIFA'),
        ('4', '4-TOIFA'),
    )
    oz = models.CharField(max_length=50, unique=True)
    uz = models.CharField(max_length=50, unique=True)
    ru = models.CharField(max_length=50, unique=True)
    en = models.CharField(max_length=50, unique=True)
    category = models.CharField(choices=AUTO_CATEGORY, max_length=2)

    def __str__(self):
        return self.oz

class Deriction(models.Model):
    a_deriction = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='aderiction')
    b_deriction = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='bderiction')
    c_deriction = models.ForeignKey(Province, on_delete=models.CASCADE, related_name='cderiction')

    def __str__(self):
        return f'{self.a_deriction}-{self.b_deriction}-{self.c_deriction}'
