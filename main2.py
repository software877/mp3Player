import tkinter as tk


class ScrollableTextArea(tk.Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.text_area = tk.Text(self, height=10, width=80)
        self.scrollbar_x = tk.Scrollbar(self, orient='horizontal', command=self.text_area.xview)
        self.scrollbar_y = tk.Scrollbar(self, command=self.text_area.yview)

        self.text_area.config(yscrollcommand=self.scrollbar_y.set)
        self.text_area.config(xscrollcommand=self.scrollbar_x.set)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.text_area.grid(row=0, column=0, sticky='nsew')
        self.scrollbar_x.grid(row=1, column=0, sticky='ew')
        self.scrollbar_y.grid(row=0, column=1, sticky='ns')


root = tk.Tk()
scrollable_text_area = ScrollableTextArea(root)
scrollable_text_area.pack(fill='both', expand=True)

for i in range(100):
    scrollable_text_area.text_area.insert('end', f'Line {i}\n')

root.mainloop()