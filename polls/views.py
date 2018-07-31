# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from decimal import Decimal
from .models import Quiz, Question, Choice, UserAttemptedQuiz
import unicodedata

# Create your views here.
@login_required(login_url="accounts:login")
def quiz_list(request):
    user = request.user
    user_id = user.id
    available = UserAttemptedQuiz.objects.filter(user_id=user_id)
    print('Available Count :- ',available.count())
    availableCount = available.count()
    #Common Dictionary
    content = {}
    attempt= {}
    actualquizdict = {}
    attemptedquizdict = {}
    commonkeys = {}
    remdata = {}
    changedremdata = {}
    if availableCount > 0:
        #quizdata = UserAttemptedQuiz.objects.filter(user_id=user_id).values('user', 'quiz', 'quizStatus', 'totalCorrect', 'totalQuestions', 'percentage')
        quizdata = UserAttemptedQuiz.objects.filter(user_id=user_id)
        #print(quizdata.count())
        #print(quizdata)
        attempt = quizdata
        content['attempt'] = attempt
        actualquiz = Quiz.objects.all()
        for quiz in actualquiz:
            actualquizdict[quiz.id] = quiz.id
        for quiz in attempt:
            attemptedquizdict[quiz.quiz_id] = quiz
        commondata = {k: actualquizdict[k] for k in actualquizdict if k not in attemptedquizdict}
        for key in commondata.keys():
            remdata[key] = Quiz.objects.filter(id=commondata[key])
        #changedremdata = {y:x for x,y in remdata.iteritems()}
        for key, value in remdata.iteritems():
            changedremdata[key]=value
        content['changedremdata'] = changedremdata
        # print(actualquiz)
        #print(attempt.quizStatus)
        #remainingdata = UserAttemptedQuiz.objects.filter(user_id=user_id)
        #remaining = Quiz.objects.exclude(id=remainingdata.quiz)
        #content['remaining'] = remaining
    else:
        quizzes = Quiz.objects.all()
        content['quizzes'] = quizzes
    print(content)
    # print(type(attempt))
    #print(type(actualquiz))
    # print(attempt)
    #print(actualquiz)
    # print(actualquizdict)
    # print(attemptedquizdict)
    #print(set(actualquizdict))
    #print(set(attemptedquizdict))
    # print(commondata)
    # print(type(commondata))
    # print(remdata)
    # print(changedremdata)
    # print(type(changedremdata))

    #print(quizdata.quiz)
    #print(attempt)

    #print(quizdata.quizStatus)
    #print(quizdata.quiz_id)
    #quizzes = Quiz.objects.all()
    # attempt = Quiz.objects.filter(id=quizdata.quiz_id)
    # remaining = Quiz.objects.exclude(id=quizdata.quiz_id)
    #questions = Question.objects.all()
    # return render(request, 'polls/quiz_list.html', {'quizzes': quizzes,'quizdata': quizdata,'attempt': attempt, 'remaining': remaining})
    return render(request, 'polls/quiz_list.html', {'content': content})
    #return HttpResponse("You are at polls index")

@login_required(login_url="accounts:login")
def question_list(request, quiz_id):
    #quiz_text = Quiz.objects.get(pk=quiz_id)
    questions = Question.objects.filter(quiz=quiz_id)
    print(questions.count())
    qlen = []
    for question in questions:
        qlen.append(question.id)
    #Questions length
    #qlength = questions.count()
    #print(type(qlength))
    #----------------
    quiz_id = quiz_id
    print(quiz_id)
    user = request.user
    print(user.id)
    #quizName = Quiz.objects.get(pk=quiz_id)
    return render(request, 'polls/question_list.html', {'questions': questions, 'quiz_id': quiz_id, 'qlen': qlen})

def detail(request):
    return HttpResponse("You are at detail")

@login_required(login_url="accounts:login")
def results(request, quiz_id):
    # foo_instance = Foo.objects.create(name='test')
    #UserAttemptedQuiz Begin Section
    # user = request.user
    # user_id = user.id
    # print(user_id)
    # myquiz_id = int(quiz_id)
    # print(myquiz_id)
    # userAttempt = UserAttemptedQuiz.objects.create(quiz_id=myquiz_id, user_id=user_id, quizStatus='Attempted')
    #UserAttemptedQuiz End Section
    questions = Question.objects.filter(quiz=quiz_id)
    print(questions.count())
    totalq = questions.count()
    mydata = {}
    for key in request.POST:
        value=request.POST[key]
        mydata[key] = value
    if 'csrfmiddlewaretoken' in mydata:
        del mydata['csrfmiddlewaretoken']
    answered = len(mydata.keys())
    unanswered = totalq - answered
    newdata = {int(k):v for k,v in mydata.items()}
    qdict = {}
    for question in questions:
        qdict[question.id] = question.answer
    print(qdict)
    print(newdata)
    correctly_answered = {k: qdict[k] for k in qdict if k in newdata and qdict[k] == newdata[k]}
    print(correctly_answered)
    totalcorrect = len(correctly_answered.keys())
    wrongly_answered = {k: qdict[k] for k in qdict if k in newdata and qdict[k] != newdata[k]}
    print(wrongly_answered)
    totalwrong = len(wrongly_answered.keys())
    percentage = Decimal((totalcorrect * 100) / totalq)
    print(totalq)
    print(totalcorrect)
    print(percentage)
    #UserAttemptedQuiz Begin Section
    user = request.user
    user_id = user.id
    print(user_id)
    myquiz_id = int(quiz_id)
    print(myquiz_id)
    userAttempt = UserAttemptedQuiz.objects.create(quiz_id=myquiz_id, user_id=user_id, quizStatus='Attempted', totalCorrect=totalcorrect, totalQuestions=totalq, percentage=percentage)
    #UserAttemptedQuiz End Section
    return render(request, 'polls/results.html', {'newdata': newdata, 'questions': questions, 'totalq': totalq, 'answered': answered, 'unanswered': unanswered, 'totalcorrect': totalcorrect, 'totalwrong': totalwrong, 'percentage': percentage})

def vote(request):
    return HttpResponse("You are at vote")
