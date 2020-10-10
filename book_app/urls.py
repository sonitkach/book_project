from django.urls import include, path

from rest_framework import routers

import book_app.views

router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
