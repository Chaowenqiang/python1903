from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from .models import *

# Create your views here.


def index(req):
    questions = Questions.objects.all()
    print(questions)

    return render(req, 'index.html', {'questions': questions})


def detail(req, id):
    questions = Questions.objects.get(pk=id)
    if req.method == 'GET':

        return render(req, 'detail.html', {'questions': questions})
    elif req.method == 'POST':

        c_id = req.POST.get('votes')
        c = Votes.objects.get(pk=c_id)
        c.votes += 1
        c.save()
        # choice = questions.votes_set.all()
        # print(choice)

        return HttpResponseRedirect('/result/%s/' % (id,))
        # return render(req, 'result.html', {'choice':choice})


def result(req, id):
    question = Questions.objects.get(pk=id)
    return render(req, 'result.html', {'question': question})
