from django.db import models

# Create your models here.
# jak tworzymy modele to zawsze potem python manage.py makemigrations , migrate

class Product(models.Model):
    title = models.CharField(max_length=120)# chrfields are limited
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)

    def __str__(self):
        return self.title
