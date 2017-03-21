from books.models import Book, BookForm
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

def index(request):
	return HttpResponse('books.index!')


def get_book(request, id):
	book = get_object_or_404(Book, pk = id)
	bookform = BookForm(instance = book)
	return render(request, 'books/bookform.html', {'bookform':bookform})
