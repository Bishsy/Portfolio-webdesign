from django.db import models

# Create your models here.
class Image(models.Model):

    nameImg = models.ImageField(upload_to='pics')
    aaImg = models.ImageField(upload_to='pics')
    myskills = models.CharField(max_length=50)
    mywork = models.TextField()
    wts = models.TextField()
