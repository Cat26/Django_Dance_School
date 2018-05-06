from django.db import models

# Create your models here.

class Zajecia(models.Model):
    title = models.CharField(max_length=120)# chrfields are limited
    description = models.TextField()

    def __str__(self):
        return self.title