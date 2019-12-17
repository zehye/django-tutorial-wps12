from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Hello, world.')


def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}")


def results(request, question_id):
    response = "you're looking at the results of question{}"
    return HttpResponse(response.format(question_id))


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
