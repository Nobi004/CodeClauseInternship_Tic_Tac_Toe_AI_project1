from django.urls import path
from . import views

urlpatterns = [
    path('', views.play_game, name='play_game'),
    path('reset/', views.reset_game, name='reset_game'),
]
