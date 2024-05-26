from django.urls import path ,include
#from django.conf.urls import url
from . import views

app_name = 'game'

urlpatterns = [
    path('', views.index, name='index'),
    path('aurevoir/', views.aurevoir, name='aurevoir')
]