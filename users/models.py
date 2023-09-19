from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext as _

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True)
    state_of_origin = models.CharField(max_length=255, blank=True)
    sex = models.CharField(max_length=10, blank=True)
    hobbies = models.TextField(blank=True)
    about_me = models.TextField(blank=True)
    address = models.TextField(blank=True)
    occupation = models.CharField(max_length=255, blank=True)
    department_unit = models.CharField(max_length=255, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    
    # Add these fields to relate to groups and user permissions
    groups = models.ManyToManyField(Group, related_name='custom_users')
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='custom_users_permissions',
    )
