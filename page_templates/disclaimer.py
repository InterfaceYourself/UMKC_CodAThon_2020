import json
from tkinter import ttk
import tkinter as tk


class Disclaimer:
    def __init__(self, parent, paper_width, paper_height):
        self.parent = parent
        self.paper_width = paper_width
        self.paper_height = paper_height
        self.frame = None
        self.icon_path = None
        self.title_text = None
        self.body_text = None
        self.icon = None
        self.icon_label = None
        self.title = None
        self.body = None

    def load_from_file(self, file):
        content = json.load(file)
        self.icon_path = content['icon_path']
        self.title_text = content['title_text']
        self.body_text = content['body_text']

    def create(self):
        self.frame = ttk.Frame(self.parent)

        self.icon = tk.PhotoImage(file=self.icon_path)
        self.icon_label = ttk.Label(self.frame, image=self.icon)
        self.title = ttk.Label(self.frame, text=self.title_text)
        self.body = ttk.Label(self.frame, text=self.body_text)

        self.icon_label.pack()  # place(x=10, y=100)
        self.title.pack()  # place(x=100, y=100)
        self.body.pack()  # place(x=10, y=200)

    def get_widget(self):
        return self.frame
