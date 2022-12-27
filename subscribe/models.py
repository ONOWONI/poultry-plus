from email.policy import default
from django.db import models

# Create your models here.

class TransactionRef(models.Model):
    tx_ref = models.CharField(max_length=30, default="None")
    owner_id = models.IntegerField()