from django.db import models
import datetime
from django.utils.timezone import now

class SmsModel(models.Model):
    phone_number = models.CharField(max_length=12)
    code = models.IntegerField(default=0)
    create_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.phone_number


    class Meta:
        verbose_name="Sms"
        verbose_name_plural = "Smslar"










#################
