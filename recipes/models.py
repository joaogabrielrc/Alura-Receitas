from distutils.command.upload import upload
from django.db import models

from people.models import Person


class ModelBase(models.Model):
  is_active = models.BooleanField(default=True)
  updated_at = models.DateTimeField(auto_now=True)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    abstract = True


class Recipe(ModelBase):
  person = models.ForeignKey(Person, on_delete=models.CASCADE)
  name = models.CharField(max_length=120)
  ingredients = models.TextField()
  preparation = models.TextField()
  time = models.IntegerField()
  amount = models.CharField(max_length=120)
  category = models.CharField(max_length=120)
  image = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)

  def __str__(self) -> str:
    return self.name
