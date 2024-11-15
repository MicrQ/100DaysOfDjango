import datetime
from django.utils import timezone
from django.db import models
""" Model definitions for the polls app """


class Question(models.Model):
    """ a model that represents a Question"""
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """ string representation of the model """
        return self.question_text
    
    def was_published_recently(self):
        """ returns True if the question was published recently """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    """ a model that represents user's Choice """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """ string representation of the model """
        return self.choice_text
