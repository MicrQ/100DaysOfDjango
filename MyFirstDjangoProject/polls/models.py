from django.db import models
""" Model definitions for the polls app """


class Question(models.Model):
    """ a model that represents a Question"""
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    """ a model that represents user's Choice """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
