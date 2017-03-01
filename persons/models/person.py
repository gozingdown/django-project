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
class Person(models.Model):
    people = models.Manager()
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)
