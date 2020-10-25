import tkinter as tk
from tkinter import ttk, PhotoImage

import ttkthemes
import platform
import random

from assets import names
from objects.patient import Patient
from page_templates.disclaimer import Disclaimer
from page_templates.patient_report import PatientReport
from widgets import get_symptoms


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

    sex_choices = ['M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'Other']  # o.O
    pick_sex = random.choice(sex_choices)
    if pick_sex == 'M':
        gender = 'M'
        first = names.male_names[random.randint(0, len(names.male_names) - 1)]
    elif pick_sex == 'F':
        gender = 'F'
        first = names.female_names[random.randint(0, len(names.female_names) - 1)]
    else:
        pick_again = random.randint(1, 2)
        if pick_again == 1:
            gender = 'M'
            first = names.male_names[random.randint(0, len(names.male_names) - 1)]
        else:
            gender = 'F'
            first = names.female_names[random.randint(0, len(names.female_names) - 1)]

    age = random.randint(18, 85)

    status_choices = ['Single', 'Married', 'Divorced', 'Separated', 'Widowed']
    status_pick = random.randint(1, 40)

    if age > 70:
        status_pick += age
    elif age > 50:
        status_pick += age // 2
    elif age > 40:
        status_pick -= age // 3
    elif age > 30:
        status_pick -= age // 4
    elif age <= 30:
        status_pick -= age // 3

    if status_pick <= 0:
        status_pick = 1

    if status_pick in range(1, 36):
        marital_status = status_choices[0]
    elif status_pick in range(36, 66):
        marital_status = status_choices[1]
    elif status_pick in range(66, 86):
        marital_status = status_choices[2]
    elif status_pick in range(86, 101):
        marital_status = status_choices[3]
    else:
        marital_status = status_choices[4]

    patient = Patient(
        first_name=first,
        last_name=names.last_names[random.randint(0, len(names.last_names) - 1)],
        age=age,
        sex=pick_sex,
        marital_status=marital_status,
        picture_path=f'assets/img/Patients/{gender}_{random.randint(1, 8)}_{random.randint(1, 3)}.png',
    )

    patient.set_covid_status(True)
    patient.add_symptoms(get_symptoms.gen_symptoms(patient.has_covid))

    patient_report = PatientReport(root_canvas, patient)
    patient_report.create()

    patient_report.get_widget().place(relx=.16, rely=.2)

    disclaimer_page.create()
    disclaimer_page.get_widget().place(anchor='c', relx=.5, rely=.5)

    # always at bottom
    root.mainloop()


if __name__ == '__main__':
    main()
