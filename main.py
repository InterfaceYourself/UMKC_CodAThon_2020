from tkinter import ttk, PhotoImage
import ttkthemes


class Centerer:
    def __init__(self, root):
        self.root = root
        self.callback_id = None

    def set_callback(self):
        self.root.bind('<Visibility>', self.center)

    def center(self, event):
        x = (self.root.winfo_screenwidth() - self.root.winfo_width()) // 2
        y = (self.root.winfo_screenheight() - self.root.winfo_height()) // 2
        self.root.geometry(f"+{x}+{y}")

        self.root.unbind('<Visibility>')


def main():
    root = ttkthemes.ThemedTk(theme='black')

    def move_window(event):
        root.geometry(f'+{event.x_root}+{event.y_root}')

    root.overrideredirect(True)  # removes the window bar

    centerer = Centerer(root)
    centerer.set_callback()

    core_frame = ttk.Frame(root, relief='ridge', border=1)
    core_frame.pack()

    handle_frame = ttk.Frame(core_frame, relief='raised')  # recreates the top bar
    handle_frame.pack(fill='x', expand=True)

    app_logo = PhotoImage(file='logo.gif')
    app_logo = app_logo.zoom(8)  # resize the image
    app_logo = app_logo.subsample(32)  # resample the image

    handle_frame_logo = ttk.Label(handle_frame, image=app_logo, relief='raised')
    handle_frame_logo.image = app_logo
    handle_frame_logo.pack(side='left', padx=2)

    app_title = ttk.Label(handle_frame, text=" App Title   ")
    app_title.pack(side='left', padx=2)

    close_button = ttk.Button(handle_frame, text='X', command=root.destroy)  # creates a button for the top bar to exit
    close_button.pack(side='right')

    labelframe = ttk.Frame(core_frame, relief='raised')
    labelframe.pack()

    greeting = ttk.Label(labelframe, text="Hello, World!")
    greeting.grid(row=0, column=0, columnspan=3, pady=5)

    prompt = ttk.Label(labelframe, text="Enter your name:")
    prompt.grid(row=1, column=0, padx=(5, 0))

    entry = ttk.Entry(labelframe, width=25, justify='c')
    entry.grid(row=1, column=1)

    button = ttk.Button(labelframe, text="Submit", command=lambda: greeting.config(text=f"Hello, {entry.get().title()   }!"))
    button.grid(row=1, column=2, padx=(0, 5))

    handle_frame.bind('<B1-Motion>', move_window)
    handle_frame_logo.bind('<B1-Motion>', move_window)
    app_title.bind('<B1-Motion>', move_window)

    root.mainloop()


if __name__ == '__main__':
    main()
