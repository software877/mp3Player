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

    def __init__(self):
        super().__init__()

        pygame.init()
        pygame.mixer.music.set_endevent(self.STOPPED_PLAYING)

        threading.Thread(target=self.event_listener).start()

        self.player_presenter.bind(self)

        self.geometry('400x450')
        self.configure(background='white')

        main_menu = MainMenu()
        main_menu.set_on_change_directory_click(self.open_new_directory)

        self.config(menu=main_menu)

        self.base_frame = BaseFrame(self)
        self.base_frame.tree.bind('<Double-1>', self.show_element_name)
        self.base_frame.volume.config(command=self.update_volume)
        self.base_frame.sound_length_value.config(command=self.update_label)
        self.base_frame.play_button.config(command=self.player_presenter.play)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.mainloop()

    def on_closing(self):
        self.PROGRAM_RUNS = False
        self.destroy()

    def event_listener(self):
        while self.PROGRAM_RUNS:
            for event in pygame.event.get():
                if event.type == self.STOPPED_PLAYING:
                    print("sound finished!!!")
                    self.player_presenter.stop()

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
        print(self.directory + "/" + element_name)
        self.player_presenter.set_sound_name(self.directory + "/" + element_name)
        self.player_presenter.play(start=True)

    def update_label(self, value):
        self.base_frame.sound_length_label.config(text=f"Length: {value}")

    def update_volume(self, value):
        self.base_frame.sound_volume_label.config(text=f"Volume: {value}")

    def stop(self):
        print("stop")

    def play(self, sound_name):
        pygame.mixer.music.load(sound_name)
        pygame.mixer.music.play()

        '''for i in range(0, 5):
            time.sleep(1)
            print("play")'''

    def resume(self):
        print("onResume")
        pygame.mixer.music.unpause()

    def pause(self):
        print("onPause")
        pygame.mixer.music.pause()
