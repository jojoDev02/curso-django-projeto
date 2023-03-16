from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views
from recipes.models import Category, Recipe
from django.contrib.auth.models import User



class RecipesViewsTest(TestCase):

    def test_recipe_home_views_func_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_category_views_func_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id' : 1}))
        self.assertIs(view.func, views.category)

    def test_recipe_details_view_func_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs= {'id' : 1}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_home_view_return_status_code_200_ok(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)
    
    def test_recipes_search_view_func_is_correct(self):
        view = resolve(reverse('recipes:search'))
        self.assertIs(view.func, views.search)

    def test_recipe_category_view_return_404_if_recipes_not_found(self):
        response = self.client.get(reverse('recipes:category', kwargs={'category_id' : 1}))
        self.assertEqual(response.status_code, 404)

    def test_recipes_load_search_template(self):
        response = self.client.get(reverse('recipes:search'))
        self.assertTemplateUsed(response, 'recipes/pages/search.html')


    def test_recipe_load_home_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html') 
    
    def test_recipe_home_template_loads_recipes(self):
        category = Category.objects.create(name = 'Category')

        author = User.objects.create_user(
            first_name = 'user',
            last_name = 'name',
            username = 'username',
            password = '123456',
            email = 'username@email.com')
        
        recipe = Recipe.objects.create(
            category=category,
            author=author,
            title='Recipe Title',
            description='Recipe Description',
            slug='recipe-slug',
            preparation_time=10,
            preparation_time_unit='Minutos',
            servings=5,
            servings_unit='Porções',
            preparation_steps='Recipe Preparation Steps',
            preparation_steps_is_html=False,
            is_published=True,
        )

        response = self.client.get(reverse('recipes:home'))
        response_recipes = response.context['recipes']

        self.assertEqual(response_recipes.first().title, 'Recipe Title')

        
        





