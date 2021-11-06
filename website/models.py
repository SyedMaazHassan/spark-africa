from django.db import models
from django.utils import timezone


class Lead(models.Model):
    email = models.EmailField(max_length=32, unique=True)
    registered_on = models.DateField(auto_now=True, verbose_name="Registration Date")

    def __str__(self):
        return self.email