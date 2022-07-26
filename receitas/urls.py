from django.urls import path

from .views import index_view, recipe_view


urlpatterns = [
  path('', index_view, name='index'),
  path('receitas/', recipe_view, name='recipe')
]
