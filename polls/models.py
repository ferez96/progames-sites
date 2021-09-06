"""models"""
import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    """Questions"""
    question_text = models.CharField(max_length=255, null=False)
    pub_date = models.DateTimeField('date published')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def was_published_recently(self):
        """a question is recently published if it has just been published within one day"""
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        """override string"""
        return "%s. %s" % (self.id, self.question_text)


class Choice(models.Model):
    """Choice"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255, null=False)
    votes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """override string"""
        return "%s. %s" % (self.question.id, self.choice_text)
