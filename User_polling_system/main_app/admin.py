from django.contrib import admin
from .models import Polling, Question, Choice


admin.site.register(Polling)
admin.site.register(Question)
admin.site.register(Choice)
