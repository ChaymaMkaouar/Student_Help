from django.db import models

class Game(models.Model):
    board = models.CharField(max_length=9, default=".........")  # 9 cases, '.' pour vide, 'X' ou 'O' pour les pièces

class Move(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.CharField(max_length=1)
    position_i = models.IntegerField(default=0)  # Position du coup joué (de 0 à 2)
    position_j = models.IntegerField(default=0)  # Position du coup joué (de 0 à 2)

