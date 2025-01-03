from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404
# from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Question
""" My first and the most basic django view """


def index(request: HttpRequest) -> HttpResponse:
    """ handles the root page
        Args:
            request: HttpRequest object
        Return:
            HttpResponse with simple text
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ", ".join([q.question_text for q in latest_question_list])

    # loading template and sending it as a response
    # tamplate = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }

    return render(request, 'polls/index.html', context)


def detail(request, question_id: int):
    """ handles the  detail of a question
        Args:
            request: HttpRequest object
            question_id: the id of the question
        Return:
            HttpResponse(view): details of the specified question.
    """
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/detail.html', {'question': question})



def results(request: HttpRequest, question_id: int) -> HttpResponse:
    """ handles the results of a question

        Args:
            request: HttpRequest object
            question_id (int): the id of the question
        Return:
            HttpResponse(view): results of the specified question.
    """
    response = "You're looking at the results of question %s"

    return HttpResponse(response % question_id)


def vote(request: HttpRequest, question_id: int) -> HttpResponse:
    """ handles the voting of a question

        Args:
            request: HttpRequest object
            question_id: the id of a specific question
        Return:
            HttpResponse(view): voting page of the specified question.
    """
    return HttpResponse("You're voting on question %s." % question_id)
