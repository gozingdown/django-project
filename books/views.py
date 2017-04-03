from books.models import Book, BookForm, Author
from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse

def index(request):
	return HttpResponse('books.index!')

def get_book(request, id):
    book = get_object_or_404(Book, pk = id)
    bookform = BookForm(instance = book)
    return render(request, 'books/bookform.html', {'bookform':bookform,'is_new':True})

def add_book(request):
    if request.method == 'POST':
        print request.POST
        book = BookForm(request.POST)

        bookmodel = book.save()
        print bookmodel.__dict__

        return redirect('books:books.get_book', id=bookmodel.id)
    else:
        bookform = BookForm()
        # ModelFormSet & its factory
        from django.forms import modelformset_factory
        AuthorFormSet = modelformset_factory(Author, fields=('name','title'))
        authorFormSet = AuthorFormSet(queryset=Author.objects.filter(name__istartswith='z'))
        # authorFormSet = AuthorFormSet(queryset=Author.objects.none())
        return render(request, 'books/bookform.html', {'bookform':bookform,'authorFormSet':authorFormSet})
