import tkinter as tk

from objects.page_manager import PageManager
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
    root.resizable(False, False)

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
    root_canvas.create_image(center_x, center_y, image=clip)

    EDGE_LEN = 30
    PAPER_TOP_LEFT = (EDGE_LEN, EDGE_LEN)
    PAPER_BOTTOM_RIGHT = (back.width() - EDGE_LEN, back.width() - EDGE_LEN)
    PAPER_WIDTH = PAPER_BOTTOM_RIGHT[0] - PAPER_TOP_LEFT[0]
    PAPER_HEIGHT = PAPER_BOTTOM_RIGHT[1] - PAPER_TOP_LEFT[1]

    disclaimer_page = Disclaimer(root_canvas, PAPER_WIDTH, PAPER_HEIGHT)

    with open('assets/pages/disclaimer.json') as f:
        disclaimer_page.load_from_file(f)

    def start_encounters():
        encounters.place_forget()
        statistics.place_forget()
        exit_option.place_forget()

        root_canvas.create_image(center_x, center_y, image=paper)
        root_canvas.create_image(center_x, center_y, image=clip)

        patients = [
            create_random_patient()
            for i in range(20)
        ]

        report_widgets = [
            PatientReport(root_canvas, patient)
            for patient in patients
        ]
        for report_widget in report_widgets:
            report_widget.create()

        page_manager = PageManager(root_canvas)
        page_manager.add_pages([report_widget.get_widget() for report_widget in report_widgets])

        page_manager.start()

        #root.bind('<Button-1>', lambda event: page_manager.flip_page())

    encounter_button = tk.PhotoImage(file='assets/img/menu_buttons/encounters.png')
    encounters = tk.Button(root_canvas, image=encounter_button, borderwidth=0, background='gray', command=start_encounters)
    encounters.image = encounter_button
    encounters.place(anchor='c', relx=.5, rely=.5)

    statistics_button = tk.PhotoImage(file='assets/img/menu_buttons/statistics.png')
    statistics = tk.Button(root_canvas, image=statistics_button, borderwidth=0, background='gray')
    statistics.image = encounter_button
    statistics.place(anchor='c', relx=.5, rely=.6)

    exit_button = tk.PhotoImage(file='assets/img/menu_buttons/exit.png')
    exit_option = tk.Button(root_canvas, image=exit_button, borderwidth=0, background='gray', command=root.destroy)
    exit_option.image = exit_button
    exit_option.place(anchor='c', relx=.5, rely=.7)

    # patient_report

    disclaimer_page.create()
    disclaimer_page.get_widget().place(anchor='c', relx=.5, rely=.5)

    # always at bottom
    root.mainloop()


if __name__ == '__main__':
    main()
