from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from .views import PollingList, PollingDetail, QuestionList, QuestionDetail, ChoiceList, ChoiceDetail, \
    ActivePollingList

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('active-pollings/', ActivePollingList.as_view(), name='active_polling_list'),
    path('pollings/', PollingList.as_view(), name='polling_list'),
    path('polling/<int:pk>/', PollingDetail.as_view()),
    path('questions/', QuestionList.as_view(), name='question_list'),
    path('question/<int:pk>/', QuestionDetail.as_view()),
    path('choices/', ChoiceList.as_view(), name='choice_list'),
    path('choice/<int:pk>/', ChoiceDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
