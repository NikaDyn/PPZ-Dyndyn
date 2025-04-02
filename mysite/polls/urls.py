from django.urls import path
from polls.views import question_list_view

app_name = 'polls'
urlpatterns = [
    path('', question_list_view, name='question_list'),
]
