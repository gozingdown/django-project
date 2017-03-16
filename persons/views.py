from django.http import HttpResponse, Http404
from persons.models import Person
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST,require_http_methods

def name(request, name =  'default_name'):
    html = '<html><body>name:' + name + '</body></html>'
    return HttpResponse(html)

@require_http_methods([ "GET"])
def detail(request, person_id):
    '''
    https://docs.djangoproject.com/en/1.10/topics/http/views/
    In order to show customized HTML when Django returns a 404, 
    you can create an HTML template named 404.html and place it in the top level of your template tree. 
    This template will then be served when DEBUG is set to False.
    '''
    p = get_object_or_404(Person, pk=int(person_id))
    return render(request, 'persons/detail.html', {'p':p})
