from django.db import models
import uuid
import datetime

def random_code():
    # return random.randint(100000, 999999)
    return str(uuid.uuid4().int)[0:6]

class SmsModel(models.Model):
    phone_number = models.CharField(max_length=12)
    code = models.IntegerField(default=random_code())
    create_at = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.phone_number
