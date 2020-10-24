import tkinter as tk
import ttkthemes
import platform

from movement_handler import MovementHandlerWithInvertedBounds


def main():
    # Create the root window give it a name and set its theme
    root = ttkthemes.ThemedTk(theme='black')
    root.lift()

    # scales the app in size
    root.tk.call('tk', 'scaling', 2)
    # always topmost while we edit so it doesnt disappear behind the windows ever 5 seconds
    root.attributes("-topmost", True)

    # remove the top bar. Even on macs...
    root.overrideredirect(True)
    if platform.system() == 'Darwin':
        root.overrideredirect(False)
    elif platform.system() == 'Windows':
        print('Windows detected +5 to bonus rolls')

    # Load images
    back = tk.PhotoImage(file='assets/img/clipboard/clipboard.png')
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

    movement_handler = MovementHandlerWithInvertedBounds(
        root,
        top_left=(30, 30),
        bottom_right=(back.width()-30, back.height()-30)
    )
    movement_handler.bind_callbacks()

    root.bind('<Button-2>', lambda _: root.destroy())

    # always at bottom
    root.mainloop()


if __name__ == '__main__':
    main()
