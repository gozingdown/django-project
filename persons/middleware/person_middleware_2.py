from django.shortcuts import render, get_object_or_404
from persons.models import Person

class PersonMiddlewareTwo(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print __name__+'.__call__.before'
        response = self.get_response(request)
        print __name__+'.__call__.after'
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print __name__+'.process_view.call'
        ###################Start - Test return HttpResponse instead of None
        # https://docs.djangoproject.com/en/1.10/topics/http/middleware/#process-view
        # 'If it returns an HttpResponse object, Django won't bother calling the appropriate view; it'll apply response middleware to that HttpResponse and return the result.'
        #p = get_object_or_404(Person, pk=int(1))
        #return render(request, 'persons/detail.html', {'p':p})
        ###################End - Test return HttpResponse instead of None
        return None

    def process_exception(self, request, exception):
        ##################Start - Test return HttpResponse instead of None
        '''
        Use this url in browser: http://127.0.0.1:8000/persons/detail/12/
        
        According to https://docs.djangoproject.com/en/1.10/topics/http/middleware/#process-exception:
        If it(process_view) returns an HttpResponse object, the template response and response middleware will be applied and the resulting response returned to the browser.

        Expectation: process_exception of PersonMiddlewareOne will be skipped. 
        '''
        print __name__+'.process_exception.call'
        #p = get_object_or_404(Person, pk=int(1))
        #return render(request, 'persons/detail.html', {'p':p})
        ##################End - Test return HttpResponse instead of None
        return None

'''
Summary:
1. If process_view returns HttpReponse instead of None, all the response middleware __call__s are still going to be called, but its own get_response will not be called
2. If process_exception returns HttpResponse instead of None, all the 'above level' process_exception will be skipped, but all thre response middleware __call__s are still going to be called.
'''
