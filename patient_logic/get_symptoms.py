import random
from assets import symptoms_lists as sl


def gen_symptoms(covid):
    symptoms = []
    real_symptoms = random.randint(0, 3)
    false_symptoms = random.randint(0, 3)
    if covid:
        for symptom in range(real_symptoms):
            symptoms.append(random.choice(sl.covid_symptoms))
        for symptom in range(false_symptoms):
            symptoms.append(random.choice(sl.false_symptoms))
    else:
        for symptom in range(real_symptoms):
            symptoms.append(random.choice(sl.non_covid_symptoms))
        for symptom in range(false_symptoms):
            symptoms.append(random.choice(sl.false_symptoms))

    if len(symptoms) == 0:
        symptoms.append('Recent potential contact')

    return set(symptoms)