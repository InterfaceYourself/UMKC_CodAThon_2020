class Patient:
    def __init__(self, picture_path, first_name, last_name, age, sex, marital_status):
        self.picture_path = picture_path
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex
        self.marital_status = marital_status
        self.has_covid = False
        self.symptoms = []

    def set_covid_status(self, status):
        self.has_covid = status

    def add_symptoms(self, symptoms):
        self.symptoms.extend(symptoms)
