from datetime import datetime
from django.db import models

# Create your models here.
class Contacttuber(models.Model):
    full_name=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    companyname=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    message=models.TextField(blank=True)
    created_date=models.DateTimeField(blank=True,default=datetime.now)
    
    def __str__(self):
        return self.email