from django.test import SimpleTestCase, TestCase
from family_budget.forms import *
from account.models import Account

class TestForms(TestCase):
    def setUp(self):
        testuser = Account.objects.create(email='mom@gmail.com', password='mom')
        self.test_budget = Budget.objects.create(name='t_b', description='test desc', owner=testuser)
        self.test_category = Category.objects.create(name='t_c', budget=self.test_budget)

    def test_budget_item_add(self):
        form = BudgetItemAddForm(data={
            'name': 'test',
            'price': 100,
            'description': 'desc',
            'budget': self.test_budget,
            'category': self.test_category,
            'currency': '$',
        })

        self.assertTrue(form.is_valid())

    def test_budget_item_add_no_data(self):
        form = BudgetItemAddForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)
