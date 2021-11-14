from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    # Required Fields
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # User Defined Fields

    first_name = models.CharField(max_length=128)
    middle_name = models.CharField(max_length=128, null=True, blank=True)
    last_name = models.CharField(max_length=128, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    mobile_number = models.CharField(max_length=20, null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = MyAccountManager()

    def __str__(self):
        return self.username

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True


class Cause(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    long_description = models.TextField(null=True, blank=True)
    picture = models.ImageField(upload_to='cause_images/')
    goal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rise = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cause_created_user', null=True, blank=True)
    updated_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cause_updated_user', null=True, blank=True)

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
    created_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='event_created_user', null=True, blank=True)
    updated_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='event_updated_user', null=True, blank=True)

    def __str__(self):
        return str(self.title)
