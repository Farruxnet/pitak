from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None):
        if not phone_number:
            raise ValueError('Users must have an phone_number')

        user = self.model(
            phone_number=phone_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None):
        user = self.create_user(
            phone_number,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    CHOICES = (
        ('oz', 'O\'zbek'),
        ('uz', 'Узбек'),
        ('ru', 'Руский'),
        ('en', 'Ingliz'),
    )
    phone_number = models.CharField(max_length=12, unique=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    language = models.CharField(choices=CHOICES, max_length=3)
    description = models.TextField(null=True, blank=True)
    STATUS_CHOICES = (
        ('customer', 'Mijoz'),
        ('driver', 'Haydovchi'),
    )
    DEVICE_CHOICES = (
        ('ios', 'iOS'),
        ('android', 'Android'),
    )
    status = models.CharField(choices=STATUS_CHOICES, max_length=10, null=True, blank=True)
    device = models.CharField(choices=DEVICE_CHOICES, max_length=10)
    account = models.PositiveIntegerField(default=0)
    profile_photo = models.ImageField(upload_to='images/', null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone_number

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    class Meta:
        verbose_name="Foydalanuvchi"
        verbose_name_plural="Foydalanuvchilar"
    @property
    def is_staff(self):
        return self.is_admin






















########################
