from tkinter import Frame
from tkinter import ttk
import tkinter as tk


class BaseFrame(Frame):

    tree: ttk.Treeview = None
    play_button: ttk.Button = None
    sound_length_label: ttk.Label = None
    volume: ttk.Scale = None
    sound_length_value: ttk.Scale = None
    loop_value = 0

    def __init__(self, root):
        super().__init__(master=root)

        self.tree = ttk.Treeview(self)

        self.play_button = ttk.Button(self, text="Play")

        self.xscrollbar = tk.Scrollbar(self, orient='horizontal', command=self.tree.xview)
        self.yscrollbar = tk.Scrollbar(self, command=self.tree.yview)

        self.tree.configure(xscrollcommand=self.xscrollbar.set, yscrollcommand=self.yscrollbar.set)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.tree.grid(row=0, column=0, sticky='nsew')
        self.xscrollbar.grid(row=1, column=0, sticky='ew')
        self.yscrollbar.grid(row=0, column=1, sticky='ns')

        self.play_button.grid(row=2, column=0, sticky='sew')

        scale_var = tk.DoubleVar()
        scale_var.set(5)

        self.volume_label = ttk.Label(self, text="Volume:")
        self.volume_label.grid(row=3, column=0, sticky='sew')

        self.volume = tk.Scale(self, from_=0, to=10, tickinterval=1, variable=scale_var,
                               orient=tk.HORIZONTAL)

        self.volume.grid(row=4, column=0, sticky='sew')

        self.sound_length = ttk.Label(self, text="Length:")
        self.sound_length.grid(row=5, column=0, sticky='sew')

        self.sound_length_value = tk.Scale(self, from_=0, to=10, orient=tk.HORIZONTAL)
        self.sound_length_value.grid(row=6, column=0, sticky='sew')

        self.sound_length_label = ttk.Label(self, text="Length: 50")
        self.sound_length_label.grid(row=7, column=0, sticky='sew')


        self.loop_value = tk.IntVar()

        self.isLoop = tk.Checkbutton(self, text="isLoop",
                         variable=self.loop_value,
                         onvalue=1, offvalue=0,
                         command="")

        self.isLoop.grid(row=8, column=0, sticky='sew')

        self.pack(fill='both', anchor='nw', expand=True)
