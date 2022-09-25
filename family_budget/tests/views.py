import json
from pydoc import describe
from django.test import TestCase, Client
from django.urls import reverse
from family_budget.models import *
from account.models import *

# Here I didn't write tests for every view, I showed BurgetItems for demonstration

class TestViews(TestCase):
    def setUp(self):
        client = Account.objects.all().first()
        self.index_url = reverse('family_budget:index')
        self.budget_url = reverse('family_budget:budget', args=['d32cf034e4fd4c099027b4692d90758a'])
        self.budget_item_url = reverse('family_budget:add_budget_item')

        self.test_budget = Budget.objects.create(name='t_b', description='test desc', owner=client)
        self.test_category = Category.objects.create(name='t_c', budget=self.test_budget)

    def test_index_GET(self):
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'budget/index.html')

    # def test_budget_GET(self):
    #     response = self.client.get(self.budget_url)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'budget/budget.html')

    

    def test_add_budget_item_POST(self):
        response = self.client.post(self.budget_item_url,{
            'name': 'test',
            'price': 100,
            'description': 'desc',
            'budget': self.test_budget,
            'category': self.test_category,
        })

        self.assertEqual(response.status_code, 302)

    def test_budget_item_DELETE(self):
        # That would work if in this method in views request.method == 'DELETE' was initialized
        response = self.client.delete(self.budget_item_url, json.dumps({
            'id':1
        }))

        self.assertEqual(response.status_code, 204)