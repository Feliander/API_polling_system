import datetime

from rest_framework import generics, permissions

from .models import Polling, Question, Choice
from .serializers import PollingSerializer, QuestionSerializer, ChoiceSerializer


class PollingList(generics.ListCreateAPIView):
    queryset = Polling.objects.all()
    serializer_class = PollingSerializer
    permission_classes = [permissions.IsAuthenticated]


class PollingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Polling.objects.all()
    serializer_class = PollingSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class ChoiceList(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = [permissions.IsAuthenticated]


class ChoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = [permissions.IsAuthenticated]


class ActivePollingList(generics.ListAPIView):
    queryset = Polling.objects.filter(finish_date__gt=datetime.datetime.now())
    serializer_class = PollingSerializer
