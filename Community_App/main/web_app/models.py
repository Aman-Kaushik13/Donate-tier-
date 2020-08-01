from django.db import models

# Create your models here.
class CreatePage(models.Model):
    created_on =  models.DateTimeField()
    organisation = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=500,null=True)
    location = models.CharField(max_length=20,null=True)
    image = models.ImageField(null=True, blank=True)
    