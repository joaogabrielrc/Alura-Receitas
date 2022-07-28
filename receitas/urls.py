from django.urls import path

from .views import (
  index_view, 
  recipe_view,
  recipe_detail_view,
  recipe_create_view,
  recipe_delete_view,
  recipe_update_view
)

urlpatterns = [
  path('', index_view, name='index'),
  path('recipes/<int:pk>/', recipe_detail_view, name='recipe'),
  path('recipes/create/', recipe_create_view, name='recipe_create'),
  path('recipes/', recipe_view, name='recipes'),
  path('recipes/<int:pk>/delete/', recipe_delete_view, name='delete_recipe'),
  path('recipes/<int:pk>/update/', recipe_update_view, name='edit_recipe')
]
