from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from .manager import CustomUserManager


# Create your models here.
class Users(AbstractUser):
    class GenderValues(models.TextChoices):
        MALE = 'Male', _('male')
        FEMALE = 'Female', _('female')

    email = models.EmailField(_('email address'), unique=True)
    phone = models.fields.IntegerField(_('phone number'), unique=True, null=False, blank=False)
    username = models.CharField(max_length=200, null=False, blank=False)
    gender = models.CharField(max_length=6, choices=GenderValues.choices)
    dateOfBirth = models.DateField()
    first_name = models.CharField(max_length=50, null=False, blank=False)
    second_name = models.CharField(max_length=50, null=False, blank=False)
    password = models.CharField(max_length=600, null=False, blank=False)
    REQUIRED_FIELDS = ['first_name', 'second_name']
    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    def __str__(self):
        return self.user_name
