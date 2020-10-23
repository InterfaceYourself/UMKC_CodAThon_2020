from tkinter import ttk


class GreeterWidget:
    def __init__(self, parent):
        self.parent = parent
        self.core_frame = None
        self.labelframe = None
        self.greeting = None
        self.prompt = None
        self.entry = None
        self.button = None

    def create(self):
        self.core_frame = ttk.Frame(self.parent, relief='ridge', border=1)
        self.core_frame.pack()

        self.labelframe = ttk.Frame(self.core_frame, relief='raised')
        self.labelframe.pack()

        self.greeting = ttk.Label(self.labelframe, text="Hello, World!")
        self.greeting.grid(row=0, column=0, columnspan=3, pady=5)

        self.prompt = ttk.Label(self.labelframe, text="Enter your name:")
        self.prompt.grid(row=1, column=0, padx=(5, 0))

        self.entry = ttk.Entry(self.labelframe, width=25, justify='c')
        self.entry.grid(row=1, column=1)

        self.button = ttk.Button(
            self.labelframe,
            text="Submit",
            command=self.update_name,
        )
        self.button.grid(row=1, column=2, padx=(0, 5))

    def update_name(self):
        self.greeting.config(text=f"Hello, {self.entry.get().title()}!")

    def get_frame(self):
        return self.core_frame
