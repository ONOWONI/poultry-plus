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


class Animal(models.Model):
    name = models.CharField(max_length=30)
    price_bought_per_one = models.FloatField()
    quantity = models.IntegerField()
    animal_age = models.FloatField()
    created_at = models.DateField(auto_now=True)
    alive = models.BooleanField(default=True)
    owner_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


EXPENSE_CHOICES = (
    ("feeds" , "feeds"),
    ("drugs" , "drugs"),
    ("equipment" , "equipment"),
    ("miscellaneous" , "miscellaneous")
)

class Expenses(models.Model):
    name = models.CharField(max_length=30)
    amount = models.FloatField()
    type = models.CharField(max_length=14, choices=EXPENSE_CHOICES)
    date= models.DateField(auto_now_add=True)
    owner_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


INCOME_CHOICES = (
    ("eggs" , "eggs"),
    ("meat" , "meat"),
    ("milk" , "milk"),
    ("other" , "other")
)


class Income(models.Model):
    name = models.CharField(max_length=30)
    amount = models.FloatField()
    quantity_sold = models.IntegerField()
    type = models.CharField(max_length=14, choices=INCOME_CHOICES)
    date= models.DateField(auto_now_add=True)
    owner_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)