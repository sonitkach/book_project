from rest_framework import viewsets, mixins, generics

from book_app.models import Book
from book_app.serializers import BookSerializer

class BookViewSet(  viewsets.GenericViewSet,
                    viewsets.mixins.ListModelMixin,
                    viewsets.mixins.CreateModelMixin,
                    viewsets.mixins.RetrieveModelMixin,
                    viewsets.mixins.UpdateModelMixin,
                    viewsets.mixins.DestroyModelMixin):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field = 'id'

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)
