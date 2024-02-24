from django.db import models
from django.contrib.auth.models import User
import pandas as pd


# Create your models here.

class QuizCategory(models.Model):
    category_name = models.CharField(max_length = 225)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name
    
    class Meta:
        verbose_name_plural = 'Quiz Categories'


class Quiz(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    category = models.OneToOneField(QuizCategory, on_delete=models.CASCADE)
    # age_group 
    ex_file = models.FileField(upload_to='quiz/', null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.title

    class Meta:
        verbose_name_plural = 'Quizzes'
    
        # call the function on quiz save
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.ex_file:
            self.import_quiz_from_excel()

    # function to extract excel file
    def import_quiz_from_excel(self):
        # read teh excel file
        df = pd.read_excel(self.ex_file.path)

        # iterate over the each row
        for index, row in df.iterrows():
            # extract question text, choices and correct answer from the row
            question_text = row['Question']
            choice1 = row['A']
            choice2 = row['B']
            choice3 = row['C']
            choice4 = row['D']
            correct_answer = row['Answer']
            difficulty = row['Difficulty']

            # create the question object
            question = Question.objects.get_or_create(quiz=self, text=question_text, difficulty=difficulty)

            # create choices objects
            choice_1 = Choice.objects.get_or_create(question=question[0], text=choice1, is_correct=correct_answer == 'A')
            choice_2 = Choice.objects.get_or_create(question=question[0], text=choice2, is_correct=correct_answer == 'B')
            choice_3 = Choice.objects.get_or_create(question=question[0], text=choice3, is_correct=correct_answer == 'C')
            choice_4 = Choice.objects.get_or_create(question=question[0], text=choice4, is_correct=correct_answer == 'D')


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.TextField()
    DIFF_CHOICES = [
            ("Easy", "Easy"),
            ("Moderate", "Moderate"),
            ("Difficult", "Difficult"),
    ]
    difficulty = models.CharField(choices=DIFF_CHOICES, null=True, max_length=225, default="Easy")

    def __str__(self):
        return self.text[:50]
    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.question.text[:50]}, {self.text[:20]}"