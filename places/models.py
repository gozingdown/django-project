#http://stackoverflow.com/questions/10589620/syntaxerror-non-ascii-character-xa3-in-file-when-function-returns-%C2%A3
# -*- coding: utf-8 -*- 
from __future__ import absolute_import
from __future__ import unicode_literals
from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

class Supplier(Place):
    customers = models.ManyToManyField(Place, related_name='providers')

class Random(models.Model):
    name = models.CharField(max_length=100)

class SupplierRandom(Place):
    randoms = models.ManyToManyField(Random)

'''
Some notes about model inheritance:
r = Restaurant(....)
r.save()

p = Place.objects.get(...)
r = Restaurant.objects.get(...)

r == p.restaurant
p == r.place_ptr



In the document: https://docs.djangoproject.com/en/1.10/topics/db/models/#inheritance-and-reverse-relations
It says:
    "
            Because multi-table inheritance uses an implicit OneToOneField to 
        link the child and the parent, it’s possible to move from the parent 
        down to the child, as in the above example.
            However, this uses up the name that is the default related_name 
        value for ForeignKey and ManyToManyField relations. If you are putting 
        those types of relations on a subclass of the parent model, you must 
        specify the related_name attribute on each such field. If you forget, 
        Django will raise a validation error.
    "
Explanation:
    p1 = Places.objects.get(...)
    s = Supplier(...)
    s.customers.add(p1)

For p1 to refer back to s, you may want to use p1.supplier, but p1.supplier
is 'used up' by the implicit OneToOne relationship for s's place to refer to
s. Thus you have to create a new related_name for p1 to refer to it's suppliers.

p1.supplier 

'''
##################
#Making Queries
#https://docs.djangoproject.com/en/1.10/topics/db/queries/
##################

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):              # __unicode__ on Python 2
        return self.headline
