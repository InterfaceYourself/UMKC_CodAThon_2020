import tkinter.ttk as ttk


class PatientInfo:
    def __init__(self, parent, patient):
        self.parent = parent
        self.patient = patient

        self.patient_info_frame = None
        self.patient_name = None
        self.patient_age = None
        self.patient_sex = None
        self.patient_status = None

    def create(self):
        self.patient_info_frame = ttk.Frame(self.parent)

        self.patient_name = ttk.Label(
            self.patient_info_frame,
            text=f'Name: {self.patient.last_name}, {self.patient.first_name}',
            background='#E7E5E8',
            foreground='black'
        )
        self.patient_name.pack(fill='x', expand=True)

        self.patient_age = ttk.Label(
            self.patient_info_frame,
            text=f'Age: {self.patient.age}',
            background='#E7E5E8',
            foreground='black'
        )
        self.patient_age.pack(fill='x', expand=True)

        self.patient_sex = ttk.Label(
            self.patient_info_frame,
            text=f'Sex: {self.patient.sex}',
            background='#E7E5E8',
            foreground='black'
        )
        self.patient_sex.pack(fill='x', expand=True)

        self.patient_status = ttk.Label(
            self.patient_info_frame,
            text=f'Status: {self.patient.marital_status}',
            background='#E7E5E8',
            foreground='black'
        )
        self.patient_status.pack(fill='both', expand=True)

    def get_widget(self):
        return self.patient_info_frame
