from django.db import models
from zajecia.models import Zajecia

# Create your models here.

class Zapisy(models.Model):
    CHOICELIST = Zajecia.objects.all()
    your_choice = models.ForeignKey(Zajecia, db_column='title', on_delete=models.CASCADE)
    title = str(your_choice)



    def __str__(self):
        return self.title