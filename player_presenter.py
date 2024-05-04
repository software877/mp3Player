from player_view import PlayerView
import threading


class PlayerPresenter():
    is_playing: bool = False
    is_paused: bool = False
    player_view: PlayerView | None = None
    sound_name = ""

    def __init__(self):
        pass

    def set_sound_name(self, sound):
        if sound != "/":
            self.sound_name = sound
            self.player_view.set_sound_length(sound)

    def bind(self, player_view: PlayerView):
        self.player_view = player_view

    def unbind(self):
        self.player_view = None

    def stop(self):
        self.player_view.to_the_beginning()

    def play(self, start = False):
        if start and self.sound_name != "":
            threading.Thread(target=self.player_view.play, args=[self.sound_name]).start()
            self.is_playing = True
            self.is_paused = False
            return

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

        if self.sound_name != "":
            threading.Thread(target=self.player_view.play, args=[self.sound_name]).start()
            self.is_playing = True
            self.is_paused = False
