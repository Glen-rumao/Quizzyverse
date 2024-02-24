from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Quiz, Question,QuizCategory

@login_required(login_url="login_user")
def quizzes(request):
    categories = QuizCategory.objects.all()
    print(categories)
    quiz = Quiz.objects.all()

    return render(request, "tables.html",{'category':categories,'quiz':quiz})
    # ques = Question.objects.filter(quiz=quiz)
    # print(ques)

@login_required(login_url="login_user")
def category(request,pk):
    categories = QuizCategory.objects.all()
    quiz = Quiz.objects.filter(category=pk)
    return render(request, "tables.html",{'category':categories,'quiz':quiz})

