from django.test import TestCase
#from unittest import TestCase
from books.models import Author

class AuthorTestCase(TestCase):
    '''
    Using unittest.TestCase avoids the cost of running each test in a 
    transaction and flushing the database, but if your tests interact 
    with the database their behavior will vary based on the order that 
    the test runner executes them. This can lead to unit tests that pass 
    when run in isolation but fail when run in a suite.
    '''
    def setUp(self):
        print 'setUp() called'
        Author.objects.create(name='testCase', title='TST')

    def test_get_author(self):
        author = Author.objects.get(name='testCase')
        Author.objects.create(name='testCase2', title='TST')
        self.assertEqual(author.title, 'TST')

    def test_get_author_2(self):
        print 'start'
        authors = Author.objects.all()
        for author in authors:
            print(author.name)