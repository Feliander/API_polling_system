from rest_framework import serializers

from .models import Polling, Question, Choice


class PollingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polling
        fields = ['id', 'name', 'start_date', 'finish_date', 'description']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question', 'question_type', 'polling']


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'question', 'choice_text']
