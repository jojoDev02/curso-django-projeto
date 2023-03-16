from django.test import TestCase
from django.urls import reverse

class RecipesURLsTest(TestCase):

    def test_recipe_home_url_is_ok(self):
        url = reverse('recipes:home')
        self.assertEqual(url, '/')

    def test_recipe_category_url_is_ok(sefl):
        url = reverse('recipes:category', kwargs={'category_id' : 1})
        sefl.assertEqual(url, '/recipes/category/1/')
    
    def test_recipe_details_url_is_ok(self):
        url = reverse('recipes:recipe' , kwargs={'id' : 2})
        self.assertEqual(url, '/recipes/2/')

    def test_recipe_url_search_is_ok(self):
        url = reverse('recipes:search')
        self.assertEqual(url, '/recipes/search/')