from django.db import models

# Create your models here.


class Question(models.Model):
    guestion_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.guestion_text


class Choice(models.Model):
    question = models.CharField(max_length=200)
    choice_text = models.TextField()
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
