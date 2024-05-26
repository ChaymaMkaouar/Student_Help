from django.shortcuts import render, redirect
from .models import Game

def home(request):
    return render(request, 'jeu/home.html')

def game(request):
    if request.method == 'POST':
        # Créer une instance de la partie et rediriger vers game.html
        game_instance = Game.objects.create()
        return redirect('game')  # Rediriger vers la vue de jeu
    return render(request, 'jeu/game.html')
