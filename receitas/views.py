from django.shortcuts import render


def index_view(request):
  return render(request, 'index.html')

def recipe_view(request):
  return render(request, 'receita.html')
