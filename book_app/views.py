from rest_framework import viewsets, mixins, generics
from django.views import generic

from book_app.models import Book
from book_app.serializers import BookListSerializer, BookDetailSerializer


class BookViewSet(viewsets.GenericViewSet,
                  viewsets.mixins.ListModelMixin,
                  viewsets.mixins.CreateModelMixin,
                  viewsets.mixins.RetrieveModelMixin,
                  viewsets.mixins.UpdateModelMixin,
                  viewsets.mixins.DestroyModelMixin):

    default_serializer_class = BookListSerializer
    queryset = Book.objects.all()
    #lookup_field = 'id'

    '''
    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request):
        return self.update(request, id)

    def delete(self, request):
        return self.destroy(request, id)
    '''

    serializer_classes = {
        "list": BookListSerializer,
        "create": BookDetailSerializer,
        "retrieve": BookDetailSerializer,
        "update": BookDetailSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)
