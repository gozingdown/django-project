from __future__ import absolute_import
# Register your models here.
from django.contrib import admin
from polls.models import Question

admin.site.register(Question)
