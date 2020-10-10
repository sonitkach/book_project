from rest_framework import serializers

from book_app.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'author_name', 'description', 'id')
