from django.db import models

# Create your models here.
class User(models.Model):
    id = models.IntegerField(primary_key = True)
    username = models.CharField(max_length = 100, blank = True, null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Tweet(models.Model):

    id = models.IntegerField(primary_key=True)
    question = models.TextField(max_length=1000)
    llama_answer = models.TextField(max_length=1000)
    gpt_answer = models.TextField(max_length=1000)
    labeler_answer = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.id}"