from django.db import models
from django.db.models import Model


class Contact_db(models.Model):
    Name = models.CharField(max_length=100)
    Vorname = models.CharField(max_length=100)
    Email = models.EmailField(max_length = 254)
    Nachricht = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name