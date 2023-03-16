from django.shortcuts import get_list_or_404, render
from recipes.models import Recipe

def home(request):
    recipes = Recipe.objects.filter(is_published = True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(request, category_id):
    recipes = get_list_or_404(Recipe.objects.filter(category__id = category_id, is_published = True ).order_by('-id'))

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': recipes[0].category.name
    })

def recipe(request, id):
    recipe = Recipe.objects.filter(pk=id,is_published = True).first()

    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'title' : recipe.title,
        'is_page_details': True,
    })

