from django.views.generic.detail import SingleObjectMixin

from .models import Book

class BookDetailMixin(SingleObjectMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        return context