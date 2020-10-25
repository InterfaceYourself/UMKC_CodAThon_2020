import tkinter as tk
import tkinter.ttk as ttk
import random
from widgets.patient_info import PatientInfo
from widgets import get_symptoms


class PatientReport:
    def __init__(self, parent, patient):
        self.parent = parent
        self.patient = patient
        self.patient_frame = None
        self.patient_info_widget = None
        self.patient_image = None
        self.patient_portrait = None
        self.symptoms_frame = None
        self.symptoms_frame_label = None
        self.has_covid = random.randint(0, 1)
        self.nav_frame = None

    def create(self):

        self.patient_frame = ttk.Frame(self.parent)
        pf = self.patient_frame
        self.patient_info_widget = PatientInfo(pf, self.patient)
        self.patient_info_widget.create()

        self.patient_image = tk.PhotoImage(file=self.patient.picture_path)
        self.patient_portrait = ttk.Label(pf, image=self.patient_image, background='#E7E5E8')

        self.symptoms_frame = ttk.Frame(pf)
        self.symptoms_frame_label = ttk.Label(pf, justify='c', text='___Symptoms___', background='#E7E5E8')

        self.patient_portrait.grid(row=0, column=0, sticky='news')

        self.patient_info_widget.get_widget().grid(row=0, column=1, sticky='news')

        self.symptoms_frame_label.grid(row=1, column=0, columnspan=2, sticky='news')
        self.symptoms_frame.grid(row=2, column=0, columnspan=2, sticky='news')

        symptoms = get_symptoms.gen_symptoms(self.has_covid)
        for i, symptom in enumerate(symptoms):
            symptom_label = ttk.Label(self.symptoms_frame, text=symptom, background='#E7E5E8')
            symptom_label.pack(fill='both', expand=True)

        self.button1 = ttk.Button(self.parent, text='<')
        self.button1.place(relx=.08, rely=.9)

        self.button2 = ttk.Button(self.parent, text='Order Test')
        self.button2.place(anchor='n', relx=.5, rely=.9)

        self.button3 = ttk.Button(self.parent, text='>')
        self.button3.place(anchor='ne', relx=.92, rely=.9)

    def get_widget(self):
        return self.patient_frame
