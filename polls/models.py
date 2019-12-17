import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    # 이 Question의 pub_date가 (현재시간 -1일) 보다 크거나 같은지 여부
    # 현재시간에서 1을 뺀날보다 크면 24시간 내에 작성된 것이라는것을 의미


class Choice(models.Model):
    # choice 여러개에 question 하나를 연결 -> foreignkey
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
