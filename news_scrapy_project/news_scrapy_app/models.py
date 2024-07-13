from django.db import models

# Create your models here.
from django.contrib.auth.models import User

# Create your models here.
STATE_CHOICES=((
    'KARACHI','KARACHI'
),('Bahalwalpur','Bahalwalpur'),('hasilpur','hasilpur'),('jamalpur','jamalpur'))
class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    Number=models.IntegerField()
    city=models.CharField(max_length=12)
    address=models.CharField(max_length=15)
    state=models.CharField(choices=STATE_CHOICES,max_length=20)
    def __str__(self):
        return str(self.id)
