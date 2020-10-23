from tkinter import ttk, PhotoImage
import ttkthemes
import datetime
import platform

from greeter_widget import GreeterWidget


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
    def move_window(event):
        root.geometry(f'+{event.x_root}+{event.y_root}')

    root = ttkthemes.ThemedTk(theme='black')
    root.iconbitmap("./assets/img/icon_w_background.ico")
    root.title("Greeter")
    root.lift()
    root.attributes("-topmost", True)
    # remove the top bar. Even on macs...
    root.overrideredirect(True)
    if platform.system() == 'Darwin':
        root.overrideredirect(False)
    elif platform.system() == 'Windows':
        print('Windows detected +5 to bonus rolls')

    centerer = Centerer(root)
    centerer.set_callback()

    master_container = ttk.Frame(root, relief='raised', border=5)
    master_container.pack()
    root_containter = ttk.Frame(master_container)
    root_containter.pack(fill='x', expand=True)

    handle_frame = ttk.Frame(root_containter, relief='raised')  # recreates the top bar
    handle_frame.pack(fill='x', expand=True)

    app_logo = PhotoImage(file='assets/img/logo.gif')
    app_logo = app_logo.zoom(8)  # resize the image
    app_logo = app_logo.subsample(32)  # resample the image

    handle_frame_logo = ttk.Button(handle_frame,
                                   image=app_logo,
                                   command=lambda: print('File menu:')
                                   )
    handle_frame_logo.image = app_logo
    handle_frame_logo.pack(side='left')

    app_title = ttk.Label(handle_frame, text=" App Title   ")
    app_title.pack(side='left', padx=2)

    close_button = ttk.Button(handle_frame, text='X', command=root.destroy)  # creates a button for the top bar to exit
    close_button.pack(side='right')

    tab_controller = ttk.Notebook(root_containter)
    tab_controller.pack(expand=True, fill='both')

    other_tab_label = ttk.Label(tab_controller, text='Where be dis?', relief='sunken')
    other_tab_label.pack()

    other_tab_label2 = ttk.Label(tab_controller, text='Where be dis?', relief='sunken')
    other_tab_label2.pack()

    greeter_widget = GreeterWidget(tab_controller)
    greeter_widget.create()

    tab_controller.add(greeter_widget.get_frame(), text='main')
    tab_controller.add(other_tab_label, text='other')
    tab_controller.add(other_tab_label2, text='stash')

    status_bar = ttk.Frame(master_container, relief='sunken')
    status_bar.pack(fill='both', expand=True)

    date_label = ttk.Label(status_bar, text=str(datetime.datetime.today()).split(' ')[0])
    date_label.pack(side='right', pady=2, padx=2)

    handle_frame.bind('<B1-Motion>', move_window)
    handle_frame_logo.bind('<B1-Motion>', move_window)
    app_title.bind('<B1-Motion>', move_window)

    root.mainloop()


if __name__ == '__main__':
    main()
