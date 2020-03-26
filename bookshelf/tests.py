import json

from django.urls import reverse
from rest_framework.test import APITestCase

from .models import Book, User


class UserTestCase(APITestCase):
    url = reverse('bookshelf:users')
    fixtures = ['users.json']

    def test_list_users(self):
        self.response = self.client.get(self.url)
        self.assertEqual(200, self.response.status_code)
        self.content = json.loads(self.response.content)
        self.assertEqual(User.objects.count(), len(self.content))

    def test_create_user(self):
        self.before_content = json.loads(self.client.get(self.url).content)
        self.response = self.client.post(self.url, {'name': 'Kirill Hulin'})
        self.single_content = json.loads(self.response.content)
        self.assertEqual(201, self.response.status_code)
        self.after_content = json.loads(self.client.get(self.url).content)
        self.assertEqual(self.after_content, [
            *self.before_content,
            self.single_content,
        ])
