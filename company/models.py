from django.db import models

# Create your models here.
class order(models.Model):
    order_id=models.CharField(unique=True,max_length=100)
    order_amount=models.PositiveBigIntegerField()
    statu=[('FAILED','failed'),('SUCESS','SUCESS'),('pending','pending')]
    status=models.CharField(choices=statu,default='pending',max_length=30)