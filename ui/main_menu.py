from tkinter import Menu
from tkinter.filedialog import askdirectory


class MainMenu(Menu):

    def open_new_directory(self):
        self.directory = askdirectory()
        print(self.directory)

    def __init__(self):
        super().__init__()

        self.directory = None
        self.file_menu = Menu(self, tearoff=0)
        self.tools_menu = Menu(self, tearoff=0)
        #self.file_menu.add_command(label="Change Directory", command=self.open_new_directory)

        self.add_cascade(label="File",
                         menu=self.file_menu)

        self.add_cascade(label="Tools",
                         menu=self.tools_menu)

    def set_on_hide_music_list(self, hide_music_list):
        self.tools_menu.add_command(label="Hide/Show music list", command=hide_music_list)

    def set_on_change_directory_click(self, open_new_directory):
        self.file_menu.add_command(label="Change Directory", command=open_new_directory)
