from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

import book_app.views

router = routers.DefaultRouter()
router.register(r'books', book_app.views.BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
