# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
#from django.utils import timezone

# Create your models here.
class Quiz(models.Model):
    quiz_text = models.CharField(max_length=200)
    users = models.ManyToManyField(User, through='UserAttemptedQuiz')

    def __str__(self):
        return self.quiz_text

class UserAttemptedQuiz(models.Model):
    quiz = models.ForeignKey(Quiz)
    user = models.ForeignKey(User)
    quizStatus = models.CharField(max_length=200)

    def __str__(self):
        return self.user,'',self.quizStatus,'',self.quiz


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    answer = models.CharField(max_length=200, default=None)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, default=None)
    #pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=None)
    #votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
