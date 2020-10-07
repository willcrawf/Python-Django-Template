from django.db import models
from django.urls import reverse

class Game(models.Model):
  title = models.CharField(max_length=100)
  release_date = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  genre = models.CharField(max_length=100)
  
  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('detail', kwargs={'game_id': self.id})