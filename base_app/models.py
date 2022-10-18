from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime

datetime.utcnow()

SCALE_CHOICES = (
    ("SMALL", "SMALL"),
    ("MEDIUM", "MEDIUM"),
    ("LARGE", "LARGE"),
)



class CustomUser(AbstractUser):
    farmerScale = models.CharField(max_length=6, choices=SCALE_CHOICES,default = "SMALL", blank=True)
    def __str__(self):
        return self.username



ANIMAL_CHOICES = (
    ("Chicken" , "Chicken"),
    ("Fish" , "Fish"),
    ("Turkey" , "Turkey"),
    ("Cow" , "Cow"),
    ("Goat" , "Goat"),
    ("Sheep" , "Sheep"),
    ("other" , "other"),
)

class Animal(models.Model):
    animal = models.CharField(max_length=8, choices=ANIMAL_CHOICES)
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
    ("miscellaneous" , "miscellaneous"),
)

class Expenses(models.Model):
    name = models.CharField(max_length=30)
    amount = models.FloatField()
    category = models.CharField(max_length=14, choices=EXPENSE_CHOICES)
    date= models.DateField(auto_now_add=True)
    owner_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


INCOME_CHOICES = (
    ("eggs" , "eggs"),
    ("meat" , "meat"),
    ("milk" , "milk"),
    ("other" , "other"),
)


class Income(models.Model):
    name = models.CharField(max_length=30)
    amount = models.FloatField()
    quantity_sold = models.IntegerField()
    category = models.CharField(max_length=14, choices=INCOME_CHOICES)
    date= models.DateField(auto_now_add=True)
    owner_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)