from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Book
from .forms import BookForm, ReviewForm


class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    paginate_by = 5

    def get_queryset(self):
        q = self.request.GET.get('q')
        if q:
            return Book.objects.filter(
                Q(title__icontains=q) |
                Q(author__icontains=q) |
                Q(genre__icontains=q)
            )
        return Book.objects.all()


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form'] = ReviewForm()
        return ctx

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = self.object
            review.user = request.user
            review.save()
        return redirect('book_detail', pk=self.object.pk)


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book_list')


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book_list')


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')
