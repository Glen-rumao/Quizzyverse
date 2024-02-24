from django.db import models
from django.contrib.auth.models import User
from home.models import QuizCategory
# Create your models here.

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    age = models.PositiveIntegerField(null = True)
    LEVEL_CHOICES = [
            ("level-1", "level-1"),
            ("level-2", "level-2"),
            ("level-3", "level-3"),
            ("level-4", "level-4")
    ]
    level = models.CharField(max_length= 225, choices=LEVEL_CHOICES, default ="level-1")
    score = models.IntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    

class Referral(models.Model):
    referring_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='referring_user')
    referred_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='referred_user')
    timestamp = models.DateTimeField(auto_now_add=True)
