import random

from assets import names
from objects.patient import Patient
from patient_logic import get_symptoms


def create_random_patient():
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

    patient.set_covid_status(random.choice([True, False]))
    patient.add_symptoms(get_symptoms.gen_symptoms(patient.has_covid))

    return patient
