from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass
 
class Donate(models.Model):
    name = models.CharField(max_length= 30)
    number = models.CharField(max_length=10)
    amount = models.IntegerField()
    order_id = models.CharField(max_length=70)

    def __str__(self):
        return f"{self.name} - {self.number} - {self.amount} - {self.order_id}"
    