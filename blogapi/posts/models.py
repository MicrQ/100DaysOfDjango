from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
    """ represents a blog post """

    title = models.CharField(max_length=50)
    body = models.TextField()
    author = models.ForeignKey(get_user_model(),
                               on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
