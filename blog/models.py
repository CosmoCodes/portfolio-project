from django.db import models
from datetime import datetime

# Create your models here.
class Blog(models.Model):
    title =models.CharField(max_length=100,default='00000')
    pub_date = models.DateTimeField(default=datetime.now())
    body=models.TextField(default='00000')
    image =models.ImageField(upload_to='images/',default='/media/images/index.jpeg')
