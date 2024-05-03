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

        self.base_frame.volume.config(command=self.update_volume)
        self.base_frame.sound_length_value.config(command=self.update_label)

        self.mainloop()


    def open_new_directory(self):
        self.directory = askdirectory()
        self.fill_tree()
        print(self.directory)

    def fill_tree(self):
        self.base_frame.tree.heading('#0', text=self.directory, anchor='w')
        #for i in range(100):
            #self.base_frame.tree.insert("", "end", text=f"Row {i}")

    def update_label(self, value):
        self.base_frame.sound_length_label.config(text=f"Length: {value}")

    def update_volume(self, value):
        self.base_frame.sound_volume_label.config(text=f"Volume: {value}")

