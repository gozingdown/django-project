from django.http import HttpResponse, Http404
from persons.models import Person
from django.shortcuts import render, get_object_or_404,redirect
from django.views.decorators.http import require_POST,require_http_methods
from persons.forms import NameForm, ContactForm
from  django.forms import formset_factory

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

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            # IMPORTANT!!
            # Since you have name-spaced url configuration, 
            # you need to mention namespace:view-name pattern in order to reverse it properly (especially from view).
            # you cannot use redirect('persons-thanks', form.cleaned_data['your_name'])
            return redirect('persons:persons-thanks', form.cleaned_data['your_name'])
    else:
        form = NameForm()
        #http://stackoverflow.com/questions/604266/django-set-default-form-values
        form2 = ContactForm(initial = {'message':'initial message'})
        # form set:
        NameFormSet = formset_factory(NameForm, extra=2, max_num=1)
        nameFormSet = NameFormSet(initial=[{'your_name':'default_your_name_1'},{'your_name':'default_your_name_2'}])
        for nameForm in nameFormSet:
            print(nameForm)
    return render(request,'persons/name.html', {'form':form, 'form2':form2})

def thanks(request, name):
    return render(request, 'persons/thanks.html', {'name':name})
