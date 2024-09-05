from game.serializers import TournamentSerializer
from main_utils.views import BaseView

from game.models import Game, Tournament
from game.serializers import GameSerializer 


class GameView(BaseView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class TournamentView(BaseView):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer 
