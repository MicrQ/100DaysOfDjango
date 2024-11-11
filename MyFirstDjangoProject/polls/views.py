from django.shortcuts import render
from django.http import HttpResponse
""" My first and the most basic django view """


def index(request):
    """ handles the root page
        Args:
            request: HttpRequest object
        Return:
            HttpResponse with simple text
    """
    return HttpResponse("Welcome to polls app!")


def detail(request, question_id: int):
    """ handles the  detail of a question
        Args:
            request: HttpRequest object
            question_id: the id of the question
        Return:
            HttpResponse(view): details of the specified question.
    """
    response = "You're looking at the results of question %s"

    return HttpResponse(response % question_id)


def results(request, question_id: int):
    """ handles the results of a question

        Args:
            request: HttpRequest object
            question_id (int): the id of the question
        Return:
            HttpResponse(view): results of the specified question.
    """
    response = "You're looking at the results of question %s"

    return HttpResponse(response % question_id)


def vote(request, question_id: int):
    """ handles the voting of a question

        Args:
            request: HttpRequest object
            question_id: the id of a specific question
        Return:
            HttpResponse(view): voting page of the specified question.
    """
    return HttpResponse("You're voting on question %s." % question_id)
