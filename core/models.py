from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Subscribe(models.Model):
	subscriber = models.ManyToManyField(User)
