from django.shortcuts import get_object_or_404, render

from receitas.models import Recipe


def index_view(request):
  recipe_queryset = Recipe.objects.filter(is_active=True).order_by('created_at')
  context = {
    'recipes': recipe_queryset
  }
  return render(request, 'index.html', context)


def recipe_view(request, pk=None):
  recipe_object = get_object_or_404(Recipe, pk=pk)  
  context = {
    'recipe': recipe_object
  }
  return render(request, 'receita.html', context)
