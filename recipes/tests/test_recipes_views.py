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