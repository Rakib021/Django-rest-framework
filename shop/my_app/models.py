from django.db import models

# Create your models here.
class Shoplist(models.Model):
  name = models.CharField(max_length=200)
  description = models.TextField(max_length=200)
  active = models.BooleanField(default=False)