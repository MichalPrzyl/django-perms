from main_utils.views import BaseView

from game.models import Game
from game.serializers import GameSerializer

class GameView(BaseView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
