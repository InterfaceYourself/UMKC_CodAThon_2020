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
        """moves the window if mouse button one is held on the top bar"""
        root.geometry(f'+{event.x_root}+{event.y_root}')

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

    # center the window when it becomes visible
    centerer = Centerer(root)
    centerer.set_callback()

    # maybe away around needing to stack containers like this
    master_container = ttk.Frame(root, relief='raised', border=5)
    master_container.pack()

    # but it gives it a nice look
    root_container = ttk.Frame(master_container)
    root_container.pack(fill='x', expand=True)

    # recreates the top bar
    handle_frame = ttk.Frame(root_container, relief='raised')
    handle_frame.pack(fill='x', expand=True)

    # Que up and resize the logo
    app_logo = PhotoImage(file='assets/img/logo.png')
    app_logo = app_logo.zoom(8)  # resize the image
    app_logo = app_logo.subsample(32)  # resample the image

    # apply the logo to the top bar left hand button
    handle_frame_logo = ttk.Button(
        handle_frame,
        image=app_logo,
        command=lambda: print('File menu:'),
    )
    handle_frame_logo.image = app_logo
    handle_frame_logo.pack(side='left', fill='y')

    # display the name of the app
    app_title = ttk.Label(handle_frame, text=" Covid Catcher   ")
    app_title.pack(side='left', padx=2)

    # treasure does not lie here
    close_button = ttk.Button(handle_frame, text='X', command=root.destroy)  # creates a button for the top bar to exit
    close_button.pack(side='right')

    # Create and pack tab controller
    tab_controller = ttk.Notebook(root_container)
    tab_controller.pack(expand=True, fill='both')

    # ---
    other_tab_label = ttk.Label(tab_controller, text='Where be dis?', relief='sunken')
    other_tab_label.pack()

    # mimic of 'other_tab_label' safe to delete
    image2 = PhotoImage(file='assets/img/clipboard/clipboardx2.png')
    other_tab_label2 = ttk.Label(tab_controller, image=image2, relief='sunken')
    other_tab_label2.image = image2
    other_tab_label2.pack()

    # Create a greeter widget and put it in root
    greeter_widget = GreeterWidget(tab_controller, root)
    greeter_widget.create()

    # Add all the items to their respective tabs
    tab_controller.add(greeter_widget.get_frame(), text='Incoming')
    tab_controller.add(other_tab_label, text='Seen')
    tab_controller.add(other_tab_label2, text='Statistics')

    # display a status bar at the bottom of the window
    status_bar = ttk.Frame(master_container, relief='sunken')
    status_bar.pack(side='bottom', fill='both', expand=True)

    # Label for current day for status bar
    status_label_date = ttk.Label(status_bar, text=str(datetime.datetime.today()).split(' ')[0])
    status_label_date.pack(side='right', pady=2, padx=2)

    # Label for whoever is logged in
    status_label_name = ttk.Label(status_bar, text='Locked')
    status_label_name.pack(side='left', pady=2, padx=2)

    # bindings to allow the movement of the window with the custom top bar
    handle_frame.bind('<B1-Motion>', move_window)
    handle_frame_logo.bind('<B1-Motion>', move_window)
    app_title.bind('<B1-Motion>', move_window)

    # always at bottom
    root.mainloop()


if __name__ == '__main__':
    main()
