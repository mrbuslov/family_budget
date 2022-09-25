# python manage.py test family_budget
from django.test import TestCase
from account.models import Account
from family_budget.models import Budget

class TestAppModels(TestCase):

    # @classmethod
    # def setUpTestData(cls):      -> will setup for the whole TestCase, not for individual method

    def setUp(self):
        testuser = Account.objects.create(email='mom@gmail.com', password='mom')
        self.budget = Budget.objects.create(name='Test', description='Test desc')


    def test_model_str(self):
        self.assertEqual(str(self.budget), 'Test') # test __str__ method

    def test_budget_like_user(self):
        self.assertEqual(Budget.objects.count(), 1)