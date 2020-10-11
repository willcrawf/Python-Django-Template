from django.db import models
from django.urls import reverse
import datetime
from django.contrib.auth.models import User



class Game(models.Model):
  title = models.CharField(max_length=100)
  release_date = models.DateField('release date')
  genre = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
def __str__(self):  
    return self.title

def get_absolute_url(self):
    return reverse('detail', kwargs={'game_id': self.id})

game = models.ForeignKey(Game, on_delete=models.CASCADE)

