from django.urls import path
from polls.views import question_list_view
from .views import register_view

app_name = 'polls'
urlpatterns = [
    path('', question_list_view, name='question_list'),
    path('register/', register_view, name='register'),
]
