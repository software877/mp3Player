import os
import tkinter as tk

from player_view import PlayerView
from player_presenter import PlayerPresenter
from ui.base_frame import BaseFrame
from ui.main_menu import MainMenu
from tkinter.filedialog import askdirectory


class MainWindow(tk.Tk, PlayerView):

    player_presenter = PlayerPresenter()
    base_frame: BaseFrame = None
    directory = ""

    def __init__(self):
        super().__init__()

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

        self.mainloop()

    def choose_directory(self):
        directory = askdirectory()

        for item in self.base_frame.tree.get_children(''):
            self.base_frame.tree.delete(item)
        for root, dirs, files in os.walk(directory):
            for file in files:
                relpath = os.path.relpath(os.path.join(root, file), start=directory)
                self.base_frame.tree.insert('', 'end', text=relpath)

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
        print(element_name)

    def update_label(self, value):
        self.base_frame.sound_length_label.config(text=f"Length: {value}")

    def update_volume(self, value):
        self.base_frame.sound_volume_label.config(text=f"Volume: {value}")

