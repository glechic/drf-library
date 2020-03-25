from django.urls import path

from rest_framework import routers

from .views import UserList, BookList

router = routers.SimpleRouter()
router.register('books', BookList)

urlpatterns = [
    path('users/', UserList.as_view()),
    *router.urls,
]
