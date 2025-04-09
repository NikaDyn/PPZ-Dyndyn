from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Question
from .forms import RegistrationForm, UserLoginForm
from .serializers import QuestionSerializer


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


def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('polls:question_list')
    else:
        form = UserLoginForm()

    return render(request, 'polls/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


class QuestionListView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)
