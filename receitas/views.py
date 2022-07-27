from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from receitas.models import Recipe


@login_required
def index_view(request):
  query = request.GET.get('q')    
  recipe_queryset = Recipe.objects.filter(is_active=True).order_by('-created_at')
  if query is not None:
    recipe_queryset = Recipe.objects.filter(is_active=True, name__icontains=query).order_by('-created_at')
  context = {
    'recipes': recipe_queryset
  }
  return render(request, 'pages/index.html', context)


@login_required
def recipe_view(request, pk=None):
  recipe_object = get_object_or_404(Recipe, pk=pk)    
  recipe_image = recipe_object.image.url
  if recipe_object.image.name == recipe_object.image.field.default:
    recipe_image = '/media/tomate_banner.jpg'      
  context = {
    'recipe': recipe_object,
    'recipe_image': recipe_image
  }
  return render(request, 'pages/recipe.html', context)
