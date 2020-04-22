from django.db import models
from datetime import datetime

# Create your models here.
class Blog(models.Model):
    title =models.CharField(max_length=100,default='00000')
    pub_date = models.DateTimeField(default=datetime.now())
    body=models.TextField(default='00000')
    image =models.ImageField(upload_to='images/',default='/media/images/index.jpeg')

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime("%b %e %Y")
