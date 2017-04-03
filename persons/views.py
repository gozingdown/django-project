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

        # Formset 1:
        # if len(initial) > max_num, max_num will not be used
        NameFormSet = formset_factory(NameForm, extra=2, max_num=3)
        nameFormSet = NameFormSet(initial=[{'your_name':'default_your_name_1'},{'your_name':'default_your_name_2'}])
        for nameForm in nameFormSet:
            print(nameForm)
        print("----------management_form")
        #https://docs.djangoproject.com/en/1.10/topics/forms/formsets/#understanding-the-managementform
        print(nameFormSet.management_form)
        print("----------management_form end")
        # Formset 2:
        NameFormSet2 = formset_factory(NameForm, max_num=2)
        data = {
            'form-TOTAL_FORMS' : '2',
            'form-INITIAL_FORMS': '0',
            'form-MAX_NUM_FORMS': '',
            'form-0-your_name' : 'adsfasfadsfasdfasd',
            'form-1-your_name' : '',#missing but will pass validation
        }
        nameFormSet2 = NameFormSet2(data)
        for nameForm in nameFormSet2:
            print(nameForm)
        print(nameFormSet2.is_valid()) 
        '''
        Note: even though form-1-your_name is missing, the validation still passes, because (from docs):
        "However, form fields of formsets won't include the required attribute as that validation 
        may be incorrect when adding and deleting forms."
        '''
        print(nameFormSet2.errors)
    return render(request,'persons/name.html', {'form':form, 'form2':form2, 'form3':nameFormSet})

def thanks(request, name):
    return render(request, 'persons/thanks.html', {'name':name})
