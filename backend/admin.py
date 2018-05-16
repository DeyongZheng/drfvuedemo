# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from backend.models import Student, LearningHistory

admin.site.register(Student)
admin.site.register(LearningHistory)

