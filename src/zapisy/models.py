from django.db import models
from django.conf import settings
from zajecia.models import Zajecia

# Create your models here.
User = settings.AUTH_USER_MODEL

class Zapisy(models.Model):
    CHOICELIST = (
        ('J', 'Modern jazz'),
        ('B', 'Modern balet'),
        ('A', 'Afro dance'),
        ('D', 'Break dance'),
    )
    your_choice = models.CharField(max_length=1, choices=CHOICELIST, null=True)
    user = models.ForeignKey(User, null=True)

#on_delete=models.CASCADE

    def __str__(self):
        return self.your_choice
