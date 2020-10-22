from tkinter import ttk
import ttkthemes


def main():
    root = ttkthemes.ThemedTk(theme='equilux')
    root.title("Hello World")

    labelframe = ttk.LabelFrame(root)
    labelframe.pack()

    greeting = ttk.Label(labelframe, text="Hello, World!")
    greeting.grid(row=0, column=0, columnspan=3)

    prompt = ttk.Label(labelframe, text="Enter your name:")
    prompt.grid(row=1, column=0)

    entry = ttk.Entry(labelframe, width=25)
    entry.grid(row=1, column=1)

    button = ttk.Button(labelframe, text="Submit", command=lambda: greeting.config(text=f"Hello, {entry.get()}!"))
    button.grid(row=1, column=2)

    root.mainloop()


if __name__ == '__main__':
    main()
