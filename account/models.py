from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
    User = models.OneToOneField( User , related_name = 'account' , on_delete = models.CASCADE )
    Balance = models.DecimalField(default=0, max_digits=12, decimal_places=2) 

    def __str__(self):
        return str(self.User)
