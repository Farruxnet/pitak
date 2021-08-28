from django.db import models
import uuid
import datetime
import math, random
from django.utils.timezone import now
def generateOTP():
	digits = "0123456789"
	OTP = ""
	for i in range(6) :
		OTP += digits[math.floor(random.random() * 10)]
	return OTP

def random_code():
    # return random.randint(100000, 999999)
    return str(uuid.uuid4().int)[0:6]

class SmsModel(models.Model):
    phone_number = models.CharField(max_length=12)
    code = models.IntegerField(default=0)
    create_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.phone_number
