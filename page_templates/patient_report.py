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
        self.symptoms_frame = None
        self.symptoms_frame_label = None
        self.nav_frame = None
        self.should_get_test = tk.IntVar(value=0)

    def create(self):

        self.patient_frame = ttk.Frame(self.parent)
        pf = self.patient_frame
        self.patient_info_widget = PatientInfo(pf, self.patient)
        self.patient_info_widget.create()

        self.patient_image = tk.PhotoImage(file=self.patient.picture_path)
        self.patient_portrait = ttk.Label(pf, image=self.patient_image, background='#E7E5E8')
        self.patient_portrait.image = self.patient_image
        self.symptoms_frame = ttk.Frame(pf)
        self.symptoms_frame_label = ttk.Label(pf, justify='c', text='Symptoms:', background='#E7E5E8')

        self.patient_portrait.grid(row=0, column=0, sticky='news')

        self.patient_info_widget.get_widget().grid(row=0, column=1, sticky='news')

        self.symptoms_frame_label.grid(row=1, column=0, columnspan=2, sticky='news')
        self.symptoms_frame.grid(row=2, column=0, columnspan=2, sticky='news')

        for symptom in self.patient.symptoms:
            symptom_label = ttk.Label(self.symptoms_frame, text=symptom, background='#E7E5E8')
            symptom_label.pack(fill='both', expand=True)

        self.button1 = ttk.Button(self.parent, text='<')
        self.button1.place(relx=.08, rely=.9)

        self.button2 = ttk.Checkbutton(self.parent, text='Order Test', variable=self.should_get_test)
        self.button2.place(anchor='n', relx=.5, rely=.9)

        self.button3 = ttk.Button(self.parent, text='>')
        self.button3.place(anchor='ne', relx=.92, rely=.9)

    def get_widget(self):
        return self.patient_frame
