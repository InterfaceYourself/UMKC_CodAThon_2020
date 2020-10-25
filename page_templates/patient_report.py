import tkinter as tk
import tkinter.ttk as ttk
from widgets.patient_info import PatientInfo


class PatientReport:
    def __init__(self, parent, patient):
        self.parent = parent
        self.patient = patient
        self.patient_frame = None
        self.patient_info_widget = None
        self.patient_image = None
        self.patient_portrait = None

    def create(self):
        self.patient_frame = ttk.Frame(self.parent)

        self.patient_info_widget = PatientInfo(self.patient_frame, self.patient)
        self.patient_info_widget.create()

        self.patient_image = tk.PhotoImage(file=self.patient.picture_path)
        self.patient_portrait = ttk.Label(self.patient_frame, image=self.patient_image, background='#E7E5E8')

        self.patient_portrait.grid(row=0, column=0)
        self.patient_info_widget.get_widget().grid(row=0, column=1)

    def get_widget(self):
        return self.patient_frame
