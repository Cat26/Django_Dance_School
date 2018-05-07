from django.db import models
import random
import os

# Create your models here.


class Zajecia(models.Model):
    title = models.CharField(max_length=120)# chrfields are limited
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title