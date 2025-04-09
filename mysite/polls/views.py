from django.shortcuts import render, redirect
from .models import Question
from django.contrib.auth import login
from .forms import RegistrationForm


def question_list_view(request):
    questions = Question.objects.all()
    context = {"questions": questions}
    return render(request, 'polls/questions.html', context)


def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('polls:question_list')
    else:
        form = RegistrationForm()

    return render(request, 'polls/register.html', {'form': form})
