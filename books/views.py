from books.models import Book, BookForm, Author, BookCoverForm, BookCover
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

from django.views import View
class GreetingView(View):
    greeting = "Good Day"

    def get(self, request):
        return HttpResponse(self.greeting)

class MorningGreetingView(GreetingView):
    greeting = "Morning to ya"

def get_bookcover(request, id):
    bookCover = get_object_or_404(BookCover, pk = id)
    return render(request, 'books/cover_img.html', {'cover_img':bookCover.cover_img})

def add_bookcover(request):
    if request.method == 'POST':
        bookCoverForm = BookCoverForm(request.POST, request.FILES)
        if bookCoverForm.is_valid():
            bookCover = bookCoverForm.save()
            print 'just saved a BookCover'
            print bookCover.cover_img.__dict__
            return redirect('books:books.get_bookcover', id=bookCover.id)
        else:
            print 'invalid form: %s' % bookCoverForm.errors
    else:
        bookCoverForm = BookCoverForm()
    return render(request, 'books/bookcover.html', {'bookCoverForm':bookCoverForm})
