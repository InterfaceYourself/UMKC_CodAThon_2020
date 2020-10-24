from tkinter import ttk, PhotoImage


class GreeterWidget:
    def __init__(self, parent, root):
        self.root = root
        self.parent = parent
        self.core_frame = None
        self.labelframe = None
        self.logo = None
        self.greeting = None
        self.prompt = None
        self.entry = None
        self.button = None
        self.password_prompt = None
        self.password_entry = None

    def create(self):
        self.core_frame = ttk.Frame(self.parent, relief='sunken', border=1)
        self.core_frame.pack(padx=10, pady=10)

        self.labelframe = ttk.Frame(self.core_frame, relief='raised')
        self.labelframe.pack(ipady=10)

        logo_gif = PhotoImage(file='assets/img/logo.png')
        self.logo = ttk.Label(self.labelframe, image=logo_gif)
        self.logo.image = logo_gif
        self.logo.grid(row=0, column=0, columnspan=2, pady=5)

        self.prompt = ttk.Label(self.labelframe, text="      Enter your name:", justify='r')
        self.prompt.grid(row=1, column=0, padx=(5, 0))

        self.entry = ttk.Entry(self.labelframe)
        self.entry.grid(row=1, column=1, padx=(0, 5))

        self.password_prompt = ttk.Label(self.labelframe, text="Enter your password:", justify='r')
        self.password_prompt.grid(row=2, column=0, padx=(5, 0))

        self.password_entry = ttk.Entry(self.labelframe, show='*')
        self.password_entry.grid(row=2, column=1, padx=(0, 5))

        self.button = ttk.Button(self.labelframe, text="Submit", command=None)
        self.button.grid(row=3, column=0, columnspan=2, pady=(10, 0))


    def get_frame(self):
        return self.core_frame
