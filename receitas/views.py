from django.shortcuts import get_object_or_404, render

from receitas.models import Recipe


def index_view(request):
  query = request.GET.get('q')    
  recipe_queryset = Recipe.objects.filter(is_active=True).order_by('-created_at')
  if query is not None:
    recipe_queryset = Recipe.objects.filter(is_active=True, name__icontains=query).order_by('-created_at')
  context = {
    'recipes': recipe_queryset
  }
  return render(request, 'index.html', context)


def recipe_view(request, pk=None):
  recipe_object = get_object_or_404(Recipe, pk=pk)  
  context = {
    'recipe': recipe_object
  }
  return render(request, 'recipe.html', context)
