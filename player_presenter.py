from player_view import PlayerView


class PlayerPresenter():
    is_playing: bool = False
    is_paused: bool = False
    player_view: PlayerView | None = None

    def __init__(self):
        pass

    def bind(self, player_view: PlayerView):
        self.player_view = player_view

    def unbind(self):
        self.player_view = None

    def play(self):
        if self.is_playing:
            self.player_view.pause()
            self.is_paused = True
            self.is_playing = False
            return

        if self.is_paused:
            self.player_view.resume()
            self.is_paused = False
            self.is_playing = True
            return

        self.player_view.play()
        self.is_playing = True
