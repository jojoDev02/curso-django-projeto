from django.shortcuts import render
from recipes.models import Recipe

from utils.recipes.factory import make_recipe

# Create your views here.

def home(request):
    recipes = Recipe.objects.filter(is_published = True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(request, category_id):
    recipes = Recipe.objects.filter(category__id = category_id, is_published = True ).order_by('-id')
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': recipes.first().category.name
    })

def recipe(request, id):
    recipe = Recipe.objects.filter(pk=id,is_published = True).first()
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_page_details': True,
    })