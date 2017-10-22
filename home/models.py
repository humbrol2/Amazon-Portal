from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Associate(models.Model):
    user = models.OneToOneField(User)
    facility = models.CharField(max_length=5, blank=True, null=True)

