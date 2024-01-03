from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=80)
    name_eng = models.CharField(max_length=80)
    description = models.CharField(max_length=120)
    price = models.IntegerField()
    img_path = models.ImageField(max_length=255)

    def __str__(self):
        return self.name