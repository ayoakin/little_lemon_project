from django.urls import reverse, resolve
from django.test import TestCase
from . import test_restaurant_models

class MenuViewTest(TestCase):
    def test_get_restaurant(self):
        url = reverse('restaurant/')
        print (url)
