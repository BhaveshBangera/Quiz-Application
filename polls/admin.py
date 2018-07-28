# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Question, Choice, Quiz, UserAttemptedQuiz

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Quiz)
admin.site.register(UserAttemptedQuiz)
