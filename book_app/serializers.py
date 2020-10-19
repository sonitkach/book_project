from rest_framework import serializers

from book_app.models import Book

class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'author_name',)

class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'author_name', 'description', 'id')