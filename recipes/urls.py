from django.urls import path

from . import views


urlpatterns = [
  path('', views.index, name='index'),
  path('receita/<int:pk>', views.recipe, name='receita'),
  path('search', views.search, name='search')
]
