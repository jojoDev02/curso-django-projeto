from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views


class RecipeSearchViewTest(TestCase):

    def test_recipes_search_view_func_is_correct(self):
        view = resolve(reverse('recipes:search'))
        self.assertIs(view.func, views.search)

    def test_recipes_load_search_template(self):
        response = self.client.get(reverse('recipes:search')+ '?q=test')
        self.assertTemplateUsed(response, 'recipes/pages/search.html')

    def test_recipe_raises_404_if_no_search_term(self):
        response = self.client.get(reverse('recipes:search'))
        self.assertEqual(response.status_code, 404)







