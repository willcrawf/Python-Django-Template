
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
from .models import Game


# Create your views here.
# Add the following import
from django.http import HttpResponse
class GameCreate(LoginRequiredMixin, CreateView):
  model = Game
  fields = ['title', 'release_date', 'description', 'genre']
  success_url = '/games/'

  def form_valid(self, form):
    # Assign the logged in user
    form.instance.user = self.request.user
    # Let the CreateView do its job as usual
    return super().form_valid(form)

class GameUpdate(LoginRequiredMixin, UpdateView):
  model = Game
  fields = ['title', 'release_date', 'description', 'genre']
  success_url = '/games/'

class GameDelete(LoginRequiredMixin, DeleteView):
  model = Game
  success_url = '/games/'

# Define the home view
def home(request):
  return render(request,'home.html')

def about(request):
  return render(request,'about.html')

@login_required
def games_index(request):
  games = Game.objects.filter(user=request.user)
  return render(request,'games/index.html', { 'games': games })

@login_required
def games_detail(request, game_id):
  game = Game.objects.get(id=game_id)
  return render(request, 'games/detail.html',{
    'game': game
  })

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('/')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)