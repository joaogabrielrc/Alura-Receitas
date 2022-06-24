from django.db import models


class ModelBase(models.Model):
  is_active = models.BooleanField(default=True)
  updated_at = models.DateTimeField(auto_now=True)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    abstract = True


class Person(ModelBase):
  name = models.CharField(max_length=120)
  email = models.CharField(max_length=120)

  def __str__(self) -> str:
    return self.name
