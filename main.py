import tkinter as tk


from page_templates.disclaimer import Disclaimer
from page_templates.patient_report import PatientReport
from patient_logic.random_patient import create_random_patient


def main():
    # Create the root window give it a name and set its theme
    root = tk.Tk()
    root.title('Counting Covid')
    root.iconbitmap('assets/img/Untitled.ico')
    root.lift()

    # scales the app in size
    root.tk.call('tk', 'scaling', 2)
    # always topmost while we edit so it doesnt disappear behind the windows ever 5 seconds
    root.attributes("-topmost", True)
    root.resizable(False, False)

    # remove the top bar. Even on macs...
    # root.overrideredirect(True)
    # if platform.system() == 'Darwin':
    #     root.overrideredirect(False)
    # elif platform.system() == 'Windows':
    #     print('Windows detected +5 to bonus rolls')

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

    EDGE_LEN = 30
    PAPER_TOP_LEFT = (EDGE_LEN, EDGE_LEN)
    PAPER_BOTTOM_RIGHT = (back.width() - EDGE_LEN, back.width() - EDGE_LEN)
    PAPER_WIDTH = PAPER_BOTTOM_RIGHT[0] - PAPER_TOP_LEFT[0]
    PAPER_HEIGHT = PAPER_BOTTOM_RIGHT[1] - PAPER_TOP_LEFT[1]

    disclaimer_page = Disclaimer(root_canvas, PAPER_WIDTH, PAPER_HEIGHT)

    with open('assets/pages/disclaimer.json') as f:
        disclaimer_page.load_from_file(f)

    patient = create_random_patient()

    patient_report = PatientReport(root_canvas, patient)
    patient_report.create()

    patient_report.get_widget().place(relx=.16, rely=.2)

    disclaimer_page.create()
    disclaimer_page.get_widget().place(anchor='c', relx=.5, rely=.5)

    # always at bottom
    root.mainloop()


if __name__ == '__main__':
    main()
