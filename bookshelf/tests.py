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
        self.assertEqual(User.objects.count(), self.content['count'])

    def test_create_user(self):
        self.before_content = json.loads(self.client.get(self.url).content)['results']
        self.response = self.client.post(self.url, {'name': 'Kirill Hulin'})
        self.single_content = json.loads(self.response.content)
        self.assertEqual(201, self.response.status_code)
        self.after_content = json.loads(self.client.get(self.url).content)['results']
        self.assertEqual(self.after_content, [
            *self.before_content,
            self.single_content,
        ])


class BookTestCase(APITestCase):
    url = reverse('bookshelf:book-list')
    def url_detail(self, pk):
        return reverse('bookshelf:book-detail', kwargs={'pk': pk})
    fixtures = ['users.json', 'books.json']
    
    def test_list_books(self):
        self.response = self.client.get(self.url)
        self.assertEqual(200, self.response.status_code)
        self.content = json.loads(self.response.content)
        self.assertEqual(Book.objects.count(), self.content['count'])

    def test_create_book(self):
        self.before_content = json.loads(self.client.get(self.url).content)['results']
        self.response = self.client.post(self.url, {
            'title': 'The Silent Patient',
            'author': 'Michaelides Alex',
            'description': 'Alicia Berenson’s life is seemingly perfect.',
            'owner': 2,
        })
        self.single_content = json.loads(self.response.content)
        self.assertEqual(201, self.response.status_code)
        self.after_content = json.loads(self.client.get(self.url).content)['results']
        self.assertEqual(self.after_content, [
            *self.before_content,
            self.single_content,
        ])

    def test_retrieve_user_related_books(self):
        self.response = self.client.get(self.url + '?owner=2')
        self.content = json.loads(self.response.content)
        self.assertEqual(Book.objects.filter(owner__pk=2).count(), self.content['count'])
