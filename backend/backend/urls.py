from django.contrib import admin
from django.urls import path

from game.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('games', GameView.as_view()),
    path('tournaments', TournamentView.as_view()),
]
