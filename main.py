from tkinter import ttk
import ttkthemes


class Centerer:
    def __init__(self, root):
        self.root = root
        self.callback_id = None

    def set_callback(self):
        self.root.bind('<Visibility>', self.center)

    def center(self, _event):
        x = (self.root.winfo_screenwidth() - self.root.winfo_width()) // 2
        y = (self.root.winfo_screenheight() - self.root.winfo_height()) // 2
        self.root.geometry(f"+{x}+{y}")

        self.root.unbind('<Visibility>')


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


def main():
    root = ttkthemes.ThemedTk(theme='black')
    root.iconbitmap("./assets/img/icon_w_background.ico")
    root.title("Greeter")

    centerer = Centerer(root)
    centerer.set_callback()

    tab_controller = ttk.Notebook(root)
    tab_controller.pack(expand=True, fill='both')

    other_tab_label = ttk.Label(tab_controller)
    other_tab_label.pack()

    greeter_widget = GreeterWidget(tab_controller)
    greeter_widget.create()

    tab_controller.add(greeter_widget.core_frame, text='main')
    tab_controller.add(other_tab_label, text='other')

    root.mainloop()


if __name__ == '__main__':
    main()
