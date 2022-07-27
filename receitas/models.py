from email.policy import default
from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL

class ModelBase(models.Model):
  is_active = models.BooleanField(default=True)
  updated_at = models.DateTimeField(auto_now=True)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    abstract = True


class Recipe(ModelBase):  
  owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)  
  name = models.CharField(max_length=120)
  ingredients = models.TextField()
  preparation = models.TextField()
  preparation_time = models.IntegerField()
  potion = models.CharField(max_length=120)
  category = models.CharField(max_length=120)  
  image = models.ImageField(upload_to='fotos/%Y/%m/%d/', default='foto_receita.png')  

  def __str__(self) -> str:
    return self.name
