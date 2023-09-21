from django.db import models

# Create your models here.
class property_agent(models.Model):
    name=models.CharField(max_length=200)
    img=models.ImageField(upload_to='pics')