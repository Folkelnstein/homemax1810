from django.db import models
from django.contrib.auth.models import AbstractUser,Group, Permission

class Auser(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='custom_user')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user')
# Create your models here.
