from django.urls import path

from rest_framework import routers

from .views import UserList, BookList

app_name = 'bookshelf'

router = routers.SimpleRouter()
router.register('books', BookList)

urlpatterns = [
    path('users/', UserList.as_view(), name='users'),
    *router.urls,
]
