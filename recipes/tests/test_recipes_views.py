from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views


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
    
    def test_recipe_load_home_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_category_view_return_404_if_recipes_not_found(self):
        response = self.client.get(reverse('recipes:category', kwargs={'category_id' : 1}))
        self.assertEqual(response.status_code, 404)
    



