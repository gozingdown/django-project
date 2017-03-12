from __future__ import absolute_import
from __future__ import unicode_literals
from django.db import models

'''
https://docs.djangoproject.com/en/1.10/topics/db/models/#organizing-models-in-a-package
The manage.py startapp command creates an application structure that includes a models.py file. 
If you have many models, organizing them in separate files may be useful.

To do so, create a models package. 
Remove models.py and create a myapp/models/ directory with an __init__.py file 
and the files to store your models. You must import the models in the __init__.py file.
'''
class AuthorManager(models.Manager):
    def get_queryset(self):
        return super(AuthorManager, self).get_queryset().filter(role='A')

class EditorManager(models.Manager):
    def get_queryset(self):
        return super(EditorManager, self).get_queryset().filter(role='E')

class PersonQuerySet(models.QuerySet):
    def authors(self):
        return self.filter(role='A')

    #Available on both Manager and QuerySet
    authors.queryset_only = False

    def editors(self):
        return self.filter(role='E')

    #make editor available only on QuerySet.
    editors.queryset_only = True

class PersonManager(models.Manager):
    def get_queryset(self):
        return super(PersonManager, self).get_queryset()

    def dick(self):
        return self.get_queryset().filter(first_name__contains='dick')

class Person(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    role = models.CharField(max_length=1, choices=(('A', 'Author'), ('E', 'Editor')), default = 'A')
    CustomManager = PersonManager.from_queryset(PersonQuerySet)
    people = CustomManager() #default_mananger by default because it's the first manager
    authors = AuthorManager()
    editors = EditorManager()
    objects = models.Manager()

    def __str__(self):
        return 'first_name:%s,last_name:%s,role:%s' % (self.first_name, self.last_name, self.role)

    #for redirect() with model objects:
    #https://docs.djangoproject.com/en/1.10/topics/http/shortcuts/#redirect
    #URL namespace:
    #https://docs.djangoproject.com/en/1.10/topics/http/urls/#url-namespaces-and-included-urlconfs
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('persons:persons-detail', kwargs={'person_id':self.id})

    class Meta:
        #https://docs.djangoproject.com/en/1.10/topics/db/managers/#django.db.models.Model._base_manager
        base_manager_name = 'objects'


