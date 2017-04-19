from django.db import models
from django.forms import ModelForm

TITLE_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
)

class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=3, choices=TITLE_CHOICES)
    birth_date = models.DateField(blank=True, null=True)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    is_published = models.BooleanField()#if you add default=True, it will still be False when not checked, since an unchecked checkbox doesn't appear in the data of an HTML form submission.
    '''
    If an optional field doesn't appear in the form's data, 
    the resulting model instance uses the model field default, 
    if there is one, for that field. This behavior doesn't apply 
    to fields that use CheckboxInput and CheckboxSelectMultiple 
    (or any custom widget whose value_omitted_from_data() method 
    always returns False) since an unchecked checkbox doesn't appear 
    in the data of an HTML form submission. Use a custom form field 
    or widget if you're designing an API and want the default fallback 
    for a BooleanField.

    So, you cannot set a default value for is_published field here. It will not be used.
    Note, even though default value will not be used, if this field is not checked in UI, the value will be False in model when evaluated 
    since the empty value of a Form BooleanField is False.


    In this case, BooleanField of a Form will use CheckboxInput as default widget
    https://docs.djangoproject.com/en/1.10/ref/models/fields/#booleanfield
    https://docs.djangoproject.com/en/1.10/ref/forms/fields/#booleanfield



    This is new in Django 1.10.1:
    Older versions don't have the exception for CheckboxInput which means that 
    unchecked checkboxes receive a value of True if that's the model field default.



    Some additional notes:
    From Docs: If the model field has blank=True, then required is set to False on the form field. Otherwise, required=True.

    http://stackoverflow.com/questions/19328302/django-modelform-doesnt-seem-to-validate-booleanfield

    It turns out (from code inspection; the docs don't say) that model BooleanFields have blank=True set automatically 
    in their __init__ method, thus making the automatically created model form field not required. 
    This makes sense upon consideration (False counts as blank, so BooleanFields need it to be true) but it's not obvious when you just read the docs.
    
    If you want it to be required to be True, the usual form field overrides apply - declare the field yourself or 
    set its required attribute to be True somewhere before validating.
    (https://docs.djangoproject.com/en/1.10/topics/forms/modelforms/#overriding-the-default-fields)
    
    Specifically, the standard widget for a BooleanField is a checkbox. Browsers do not submit anything for unchecked checkboxes, 
    so the checkbox widget treats the absence of the field from the submit as False. There's no way to distinguish the user not 
    selecting the checkbox from cases in which the input really is bad. You could use a different widget (say, a RadioSelect) to 
    at least make it possible for the browser to submit something for False, but you still have the problem that the BooleanField's 
    to_python method converts its value to a boolean before validating, so you'd have to subclass and override.

    Fortunately, False is not considered empty by the validation code, so if you do that you'll be able to set required=True and don't need custom cleaning methods.
    '''
    def __str__(self):
        return self.name

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'title', 'birth_date']

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'authors','is_published']


class BookCover(models.Model):
    name = models.CharField(max_length=100)
    # need to install Pillow for ImageField
    cover_img = models.ImageField(upload_to='books')

class BookCoverForm(ModelForm):
    class Meta:
        model = BookCover
        fields = '__all__'
