from django.test import SimpleTestCase
from django.urls import reverse, resolve
from family_budget.views import *

class TestUrls(SimpleTestCase): # SimpleTestCase - because we don't need an access to db
    def test_index_resolve(self):
        url = reverse('family_budget:index')
        self.assertEqual(resolve(url).func,index) 

    def test_budget_resolve(self):
        url = reverse('family_budget:budget', args=['any-slug'])
        self.assertEqual(resolve(url).func,budget) 

    def test_add_budget_item_resolve(self):
        url = reverse('family_budget:add_budget_item')
        self.assertEqual(resolve(url).func,add_budget_item) 

    def test_add_category_resolve(self):
        url = reverse('family_budget:add_category')
        self.assertEqual(resolve(url).func,add_category) 
        
    def test_add_budget_resolve(self):
        url = reverse('family_budget:add_budget')
        self.assertEqual(resolve(url).func,add_budget) 