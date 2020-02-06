from django.db import models

# Create your models here.
class Farm(models.Model):
    # admin_user = models.OneToOneField()
    name = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
