from tkinter import ttk
import ttkthemes

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
