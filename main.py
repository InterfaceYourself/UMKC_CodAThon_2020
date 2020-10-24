from tkinter import ttk
import tkinter as tk
import ttkthemes
import platform


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

    root_canvas.create_image(back.width() // 2, back.height() // 2, image=back)
    root_canvas.create_image(back.width() // 2, back.height() // 2, image=paper)
    root_canvas.create_image(back.width() // 2, back.height() // 2, image=clip)

    # always at bottom
    root.mainloop()


if __name__ == '__main__':
    main()
