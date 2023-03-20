from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views

class RecipeViewDetailTest(TestCase):

    def test_recipe_details_view_func_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs= {'id' : 1}))
        self.assertIs(view.func, views.recipe)

  






