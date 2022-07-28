from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from receitas.models import Recipe


User = get_user_model()

@login_required
def recipe_view(request):  
  recipe_queryset = Recipe.objects.filter(is_active=True, owner=request.user).order_by('-created_at')  
  context = {
    'recipes': recipe_queryset
  }
  return render(request, 'pages/index.html', context)


@login_required
def recipe_create_view(request):

  if request.method == 'POST':
    user = request.user
    name = request.POST.get('name')
    ingredients = request.POST.get('ingredients')
    preparation = request.POST.get('preparation')
    preparation_time = request.POST.get('preparation_time')
    potion = request.POST.get('potion')
    category = request.POST.get('category')    
    image = request.FILES.get('image')

    recipe = Recipe.objects.create(
      owner=user, 
      name=name, 
      ingredients=ingredients,
      preparation=preparation,
      preparation_time=preparation_time,
      potion=potion,
      category=category      
    )
    if image:          
      recipe.image = image    
    recipe.save()
    return redirect('/')

  return render(request, 'pages/recipe-create.html')


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
def recipe_detail_view(request, pk=None):
  recipe_object = get_object_or_404(Recipe, pk=pk)    
  recipe_image = recipe_object.image.url
  if recipe_object.image.name == recipe_object.image.field.default:
    recipe_image = '/media/tomate_banner.jpg'      
  context = {
    'recipe': recipe_object,
    'recipe_image': recipe_image
  }
  return render(request, 'pages/recipe.html', context)
