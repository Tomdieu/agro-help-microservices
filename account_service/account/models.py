from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):

    USER_TYPES = (
        ('agriculteur', 'agriculteur'),
        ('expert', 'expert')
    )
    type = models.CharField(choices=USER_TYPES, max_length=20)
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
