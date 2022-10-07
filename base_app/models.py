# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models


SCALE_CHOICES = (
    ("SMALL", "SMALL"),
    ("MEDIUM", "MEDIUM"),
    ("LARGE", "LARGE"),
)
class CustomUser(AbstractUser):
    farmerScale = models.CharField(max_length=6, choices=SCALE_CHOICES,default = "SMALL", blank=True)
    def __str__(self):
        return self.username