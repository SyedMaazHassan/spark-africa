from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


UserModel = get_user_model()


class Lead(models.Model):
    email = models.EmailField(max_length=32, unique=True)
    registered_on = models.DateField(auto_now=True, verbose_name="Registration Date")

    def __str__(self):
        return self.email


class Contact(models.Model):
    """
    Models for contact forms
    """
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=256)
    note = models.TextField(max_length=2000)
    received_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address



class Cause(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    long_description = models.TextField(null=True, blank=True)
    picture = models.ImageField(upload_to='cause_images/')
    goal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rise = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='cause_created_user', null=True, blank=True)
    updated_user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='cause_updated_user', null=True, blank=True)

    def __str__(self):
        return str(self.title)


class EventCategory(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return str(self.title)


class Event(models.Model):
    category = models.ForeignKey(EventCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True, blank=True)
    short_description = models.TextField(null=True, blank=True)
    long_description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='events/', null=True, blank=True)
    location = models.CharField(max_length=1024, null=True, blank=True)
    start_date = models.DateTimeField(default=None)
    end_date = models.DateTimeField(default=None)
    status = models.BooleanField(default=True, blank=True)
    creation_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    creation_date = models.DateField(auto_now_add=True, blank=True, null=True)
    created_user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='event_created_user', null=True, blank=True)
    updated_user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='event_updated_user', null=True, blank=True)

    def __str__(self):
        return str(self.title)
