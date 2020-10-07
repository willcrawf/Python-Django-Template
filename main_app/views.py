from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Game
# Create your views here.
# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request,'home.html')

def about(request):
  return render(request,'about.html')

def games_index(request):
  return render(request,'games/index.html', { 'games': games })

def games_detail(request):
  return render(request, 'home.html')

# class Game:
#     def __init__(self, title, release_date, description, genre):
#         self.title = title
#         self.release_date = release_date
#         self.description = description
#         self.genre = genre

games = [
    Game('The Legend of Zelda: Breath of the Wild', '2017', 'Set in an open world where players are tasked with exploring the kingdom of Hyrule while controlling Link.', 'Adventure'),
    Game('Borderlands 2', '2012', 'Four playable character classes are available in the base game, each with their own unique Action Skill: Axton, "the Commando", can summon a turret to provide offensive support.', 'Shooter'),
]

class GameCreate(CreateView):
  model = Game
  fields = '__all__'
