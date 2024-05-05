from player_view import PlayerView
import threading


class PlayerPresenter():
    is_playing: bool = False
    is_paused: bool = False
    is_loop: bool = False
    player_view: PlayerView | None = None
    sound_name = ""
    is_button_length_pressed = False
    __sound_position_value = 0

    def __init__(self):
        pass

    def set_sound_name(self, sound):
        if sound != "/":
            self.sound_name = sound
            self.player_view.set_sound_length(sound)


    def set_pos(self):
        if self.is_playing or self.is_paused:
            self.player_view.change_sound_position(self.__sound_position_value)

    def set_sound_position_value(self, value):
        self.__sound_position_value = float(value)
        self.player_view.update_label(value)

    def set_button_pressed(self, value):
        self.is_button_length_pressed = value

    def button_length_listener(self):
        if self.is_button_length_pressed:
            print("pressed!!!")
            return
        #self.player_view.get_sound_position()

    def bind(self, player_view: PlayerView):
        self.player_view = player_view

    def loop_checkbox_clicked(self):
        self.player_view.loop_checkbox_clicked()

    def set_loop_value(self, value):
        self.is_loop = value == 1

    def unbind(self):
        self.player_view = None

    def stop(self):
        self.is_paused = False
        self.is_playing = False
        self.player_view.to_the_beginning()

    def play(self, start = False):
        loop = 0
        if self.is_loop:
            loop = -1

        if start and self.sound_name != "":
            threading.Thread(target=self.player_view.play, args=[self.sound_name, loop]).start()
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
            threading.Thread(target=self.player_view.play, args=[self.sound_name, loop]).start()
            self.is_playing = True
            self.is_paused = False
