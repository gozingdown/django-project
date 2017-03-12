from django.http import HttpResponse, Http404
from persons.models import Person

def name(request, name =  'default_name'):
    html = '<html><body>name:' + name + '</body></html>'
    return HttpResponse(html)

def detail(request, person_id):
    '''
    https://docs.djangoproject.com/en/1.10/topics/http/views/
    In order to show customized HTML when Django returns a 404, 
    you can create an HTML template named 404.html and place it in the top level of your template tree. 
    This template will then be served when DEBUG is set to False.
    '''
    try:
        p = Person.objects.get(pk=int(person_id))
    except Person.DoesNotExist:
        raise Http404('Person does not exist')
    html = '<html><body>Person:' + str(p) + '</body></html>'
    return HttpResponse(html)
