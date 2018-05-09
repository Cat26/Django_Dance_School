from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from zajecia.models import Zajecia

# Create your models here.
User = settings.AUTH_USER_MODEL

class Zapisy(models.Model):
    CHOICELIST = (
        ('1', 'Modern jazz'),
        ('2', 'Modern balet'),
        ('3', 'Afro dance'),
        ('4', 'Break dance'),
    )
    your_choice = models.CharField(max_length=1, choices=CHOICELIST, null=True)
    user = models.ForeignKey(get_user_model(), default=1)

#on_delete=models.CASCADE

    def __str__(self):
        return self.your_choice
