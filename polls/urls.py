"""basicproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

app_name = 'quiz'

urlpatterns = [
    url(r'^$', views.quiz_list, name='list'),
    url(r'^(?P<quiz_id>[0-9]+)/$', views.question_list, name='question_list'),
    #url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^results/(?P<quiz_id>[0-9]+)/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]