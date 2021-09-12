from django.db import models
from django.utils.timezone import now


class Polling(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateTimeField(editable=False, default=now())
    finish_date = models.DateTimeField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Question(models.Model):
    question = models.CharField(max_length=255)
    question_type = models.CharField(max_length=255)
    polling = models.ForeignKey('Polling', on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class Choice(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)

    def __str__(self):
        return self.choice_text
