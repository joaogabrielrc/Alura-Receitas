from django.shortcuts import render


def index_view(request):
  context = {
    'list': [{
      'name': 'Sorvete'
    }]
  }
  return render(request, 'index.html', context)


def recipe_view(request):
  return render(request, 'receita.html')
