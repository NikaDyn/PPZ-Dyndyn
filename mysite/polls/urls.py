from django.urls import path
from polls.views import *

app_name = 'polls'
urlpatterns = [
    path('', question_list_view, name='question_list'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('api/questions/', QuestionListView.as_view(), name='questions-api'),
]
