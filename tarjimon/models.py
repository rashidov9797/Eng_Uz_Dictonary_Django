from django.db import models

# Create your models here.

# class Lugat(models.Model):
#   english = models.CharField('English',max_length=60)
#   uzbek = models.CharField('O\'zbekcha',max_length=60)
  

class Lugatlar(models.Model):
  english = models.CharField('English',max_length=60)
  uzbek = models.CharField('O\'zbekcha',max_length=60)