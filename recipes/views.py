from django.shortcuts import get_object_or_404, render

from .models import Recipe


def index(request):
  data = {
    'recipes': Recipe.objects.filter(is_active=True).order_by('-updated_at')
  }

  return render(request, 'index.html', data)


def recipe(request, pk=None):
  recipe = get_object_or_404(Recipe, pk=pk)
  
  data = {
    'recipe': recipe
  }

  return render(request, 'receita.html', data)


def search(request):
  queryset = Recipe.objects.filter(is_active=True).order_by('-updated_at')
  
  if 'search' in request.GET:    
    search_param = request.GET['search']

    if search_param:
      recipes = queryset.filter(name__icontains=search_param)

  data = {
    'recipes': recipes
  }

  return render(request, 'filter.html', data)
