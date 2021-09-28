import requests
from django.test import TestCase

r = requests.get('http://127.0.0.1:8000/')
print(r.text)