from unicodedata import category
import pytest
from django.test import TestCase

from restaurant.models import Component


class ComponentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Component.objects.create(category='COLD DRINKS', component='Water', price=0.3)

    def test_category_max_length(self):
        component = Component.objects.get(component='Water')
        max_length = component._meta.get_field('category').max_length
        self.assertEquals(max_length, 25)
    
    def test_component_blank(self):
        component = Component.objects.get(component='Water')
        blank = component._meta.get_field('component').blank
        self.assertEquals(blank, True)

    def test_price_value(self):
        component = Component.objects.get(component='Water')
        price = component.price
        self.assertEquals(price, 0.3)
