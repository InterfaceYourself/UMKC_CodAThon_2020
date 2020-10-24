from tkinter import ttk
import tkinter as tk
import ttkthemes
import platform


class MovementHandler:
    def __init__(self, root):
        self.root = root
        self.previous_mouse_x = None
        self.previous_mouse_y = None

    def bind_callbacks(self):
        self.root.bind('<Button-1>', self._set_location)
        self.root.bind('<B1-Motion>', self._move)

    def _move(self, event):
        change_in_x = event.x - self.previous_mouse_x
        change_in_y = event.y - self.previous_mouse_y

        self.root.geometry(
            f'+{self.root.winfo_x() + change_in_x}'
            f'+{self.root.winfo_y() + change_in_y}'
        )

    def _set_location(self, event):
        self.previous_mouse_x = event.x
        self.previous_mouse_y = event.y


def main():
    # Create the root window give it a name and set its theme
    root = ttkthemes.ThemedTk(theme='black')
    root.lift()

    # scales the app in size
    root.tk.call('tk', 'scaling', 2)
    # always topmost while we edit so it doesnt disappear behind the windows ever 5 seconds
    root.attributes("-topmost", True)

    # remove the top bar. Even on macs...
    if platform.system() == 'Darwin':
        root.overrideredirect(False)
    elif platform.system() == 'Windows':
        root.overrideredirect(True)
        print('Windows detected +5 to bonus rolls')

    # Load images
    back = tk.PhotoImage(file='assets/img/clipboard/clipboardx2.png')
    paper = tk.PhotoImage(file='assets/img/clipboard/paper.png')
    clip = tk.PhotoImage(file='assets/img/clipboard/metal_clip.png')

    # Resize and center window based on dimensions of `back`
    root.geometry(
        f'{back.width()}x{back.height()}'
        f'+{(root.winfo_screenwidth() - back.width()) // 2}'
        f'+{(root.winfo_screenheight() - back.height()) // 2}'
    )

    root_canvas = tk.Canvas(root)
    root_canvas.pack(expand=True, fill='both')

    center_x = back.width() // 2
    center_y = back.height() // 2

    root_canvas.create_image(center_x, center_y, image=back)
    root_canvas.create_image(center_x, center_y, image=paper)
    root_canvas.create_image(center_x, center_y, image=clip)

    movement_handler = MovementHandler(root)
    movement_handler.bind_callbacks()

    # always at bottom
    root.mainloop()


if __name__ == '__main__':
    main()
