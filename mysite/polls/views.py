from django.shortcuts import render
from .models import Question


def question_list_view(request):
    questions = Question.objects.all()
    context = {"questions": questions}
    return render(request, 'questions.html', context)

