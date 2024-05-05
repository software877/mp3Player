import os
import tkinter as tk
from player_view import PlayerView
from player_presenter import PlayerPresenter
from ui.base_frame import BaseFrame
from ui.main_menu import MainMenu
from tkinter.filedialog import askdirectory
import pygame
import threading


class MainWindow(tk.Tk, PlayerView):
    player_presenter = PlayerPresenter()
    base_frame: BaseFrame = None
    directory = ""
    STOPPED_PLAYING = pygame.USEREVENT + 1
    PROGRAM_RUNS = True
    sound_length = 0

    def __init__(self):
        super().__init__()

        pygame.init()
        pygame.mixer.music.set_endevent(self.STOPPED_PLAYING)

        #threading.Thread(target=self.event_listener).start()

        self.player_presenter.bind(self)

        self.geometry('400x450')
        self.configure(background='white')

        main_menu = MainMenu()
        main_menu.set_on_change_directory_click(self.open_new_directory)

        self.config(menu=main_menu)

        self.base_frame = BaseFrame(self)
        self.base_frame.tree.bind('<Double-1>', self.show_element_name)
        self.base_frame.sound_length_value.bind('<Button-1>', self.base)
        self.base_frame.sound_length_value.bind('<ButtonRelease-1>', self.unpress)

        self.base_frame.volume.config(command=self.update_volume)
        self.base_frame.sound_length_value.config(command=self.player_presenter.set_sound_position_value)
        self.base_frame.play_button.config(command=self.player_presenter.play)

        self.base_frame.isLoop.config(command=self.player_presenter.loop_checkbox_clicked)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        threading.Thread(target=self.event_listener).start()


        self.mainloop()

    def base(self, event):
        self.player_presenter.set_button_pressed(True)
        print("clicked!!!")

    def unpress(self, event):
        self.player_presenter.set_button_pressed(False)
        self.player_presenter.set_pos()
        print("unpressed")

    def loop_checkbox_clicked(self):
        self.player_presenter.set_loop_value(self.base_frame.loop_value.get())

    def change_sound_position(self, value):
        pygame.mixer.music.set_pos(value)

    def on_closing(self):
        self.PROGRAM_RUNS = False
        self.destroy()

    def set_sound_length(self, value):
        sound = pygame.mixer.Sound(value)
        self.sound_length = sound.get_length()
        self.base_frame.sound_length_value.config(to=self.sound_length)
        print(self.sound_length)

    def event_listener(self):
        while self.PROGRAM_RUNS:
            for event in pygame.event.get():
                if event.type == self.STOPPED_PLAYING:
                    print("sound finished!!!")
                    self.player_presenter.stop()

            #self.player_presenter.button_length_listener()


    def get_sound_position(self):
        pos = pygame.mixer.music.get_pos()
        print(pos)
        #self.base_frame.sound_length_value.set(pos)

    def open_new_directory(self):
        self.directory = askdirectory()
        self.fill_tree()

    def fill_tree(self):
        self.base_frame.tree.heading('#0', text=self.directory, anchor='w')
        for item in self.base_frame.tree.get_children(''):
            self.base_frame.tree.delete(item)
        for root, dirs, files in os.walk(self.directory):
            for file in files:
                relpath = os.path.relpath(os.path.join(root, file), start=self.directory)
                self.base_frame.tree.insert('', 'end', text=relpath)

    def show_element_name(self, event):
        element_name = self.base_frame.tree.item(self.base_frame.tree.selection())['text']
        self.player_presenter.set_sound_name(self.directory + "/" + element_name)
        self.player_presenter.play(start=True)
        self.base_frame.play_button.config(text="Pause")

    def update_label(self, value):
        #pygame.mixer.music.set_pos(float(value))
        self.base_frame.sound_length_label.config(text=f"Length: {value}")

    def update_volume(self, value):
        pygame.mixer.music.set_volume(int(value) / 10)

    def stop(self):
        print("stop")

    def play(self, sound_name, is_loop = 0):
        pygame.mixer.music.load(sound_name)
        pygame.mixer.music.play(loops=is_loop)

    def resume(self):
        print("onResume")
        pygame.mixer.music.unpause()
        self.base_frame.play_button.config(text="Pause")

    def pause(self):
        print("onPause")
        self.base_frame.play_button.config(text="Play")
        pygame.mixer.music.pause()
