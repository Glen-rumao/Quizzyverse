from django.urls import path
from .views import *

urlpatterns = [
     path('quizzes/',quizzes,name='quizzes'),
     path('category/int<pk>',category,name='category'),

]