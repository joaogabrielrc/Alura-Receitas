from django.urls import path

from .views import (
  index_view, 
  recipe_view,
  recipe_detail_view,
  recipe_create_view
)


urlpatterns = [
  path('', index_view, name='index'),
  path('recipes/<int:pk>/', recipe_detail_view, name='recipe'),
  path('recipes/create/', recipe_create_view, name='recipe_create'),
  path('recipes/', recipe_view, name='recipes')
]
