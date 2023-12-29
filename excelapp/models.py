from django.db import models

class Product(models.Model):
    name = models.CharField(max_length = 20, blank = False)
    description = models.CharField(max_length = 20, blank = False)
    qnt = models.CharField(max_length = 20, blank = False)
    price = models.CharField(max_length = 20, blank = False)
    def __str__(self):
        return self.name
   



