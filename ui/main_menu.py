from tkinter import Menu


class MainMenu(Menu):
    def __init__(self):
        super().__init__()

        file_menu = Menu(self, tearoff=0)
        file_menu.add_command(label="Change Directory", command="")

        self.add_cascade(label="File",
                             menu=file_menu)



