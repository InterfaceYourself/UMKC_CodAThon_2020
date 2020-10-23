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


def main():
    root = ttkthemes.ThemedTk(theme='black')
    root.iconbitmap("./assets/img/logo.ico")
    root.title("Greeter")

    centerer = Centerer(root)
    centerer.set_callback()

    tab_controller = ttk.Notebook(root)
    tab_controller.pack(expand=True, fill='both')

    core_frame = ttk.Frame(tab_controller, relief='ridge', border=1)
    core_frame.pack()

    labelframe = ttk.Frame(core_frame, relief='raised')
    labelframe.pack()

    greeting = ttk.Label(labelframe, text="Hello, World!")
    greeting.grid(row=0, column=0, columnspan=3, pady=5)

    prompt = ttk.Label(labelframe, text="Enter your name:")
    prompt.grid(row=1, column=0, padx=(5, 0))

    entry = ttk.Entry(labelframe, width=25, justify='c')
    entry.grid(row=1, column=1)

    other_tab_label = ttk.Label(tab_controller)
    other_tab_label.pack()

    tab_controller.add(core_frame, text='main')
    tab_controller.add(other_tab_label, text='other')

    button = ttk.Button(
        labelframe,
        text="Submit",
        command=lambda: greeting.config(text=f"Hello, {entry.get().title()}!")
    )
    button.grid(row=1, column=2, padx=(0, 5))

    root.mainloop()


if __name__ == '__main__':
    main()
