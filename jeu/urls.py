from django.urls import path
from . import views
app_name = 'jeu'
urlpatterns = [
    path('', views.home, name='home'),
    path('game/', views.game, name='game'),
]
