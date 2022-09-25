from django.test import TestCase
import requests
import json



# print(requests.get('http://127.0.0.1/budget/2/').json())
headers = {'Authorization': 'Token 6429bc64b55fae3d62c5c942c03a64f17bd23ec6'}
dic = {
    'title': 'request',
    'body': 'request body',
}
print(requests.post('http://127.0.0.1/budget/', data=dic, headers=headers).json())