import tkinter as tk
from ui.main_menu import MainMenu


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('400x300')
        self.configure(background='white')

        main_menu = MainMenu()
        self.config(menu=main_menu)

        self.mainloop()
