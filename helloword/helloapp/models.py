from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    decs=models.TextField()

class profil(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='photo')
    decs=models.TextField()