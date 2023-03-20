from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views


class RecipeViewcategoryTest(TestCase):

    def test_recipe_category_views_func_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id' : 1}))
        self.assertIs(view.func, views.category)

    def test_recipe_category_view_return_404_if_recipes_not_found(self):
        response = self.client.get(reverse('recipes:category', kwargs={'category_id' : 1}))
        self.assertEqual(response.status_code, 404)

 
 