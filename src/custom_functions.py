"""This module contains custom functions used in the App"""

import a_classes as a

# define a decorator to add a date
def date_form():
    """Function to add a date to a class"""
    day = int(input('Day: '))
    month = int(input('Month: '))
    year = int(input('Year: '))
    date = a.Date(day, month, year)
    return date

def patient_form(func):
    """Decorator to add a patient"""
    def wrapper(*args):
        patient_id = int(input('Patient ID: '))
        name = input('Name: ')
        genre = input('Genre: ')
        birth_date = date_form()
        bed_number = int(input('Bed number: '))
        new_patient = a.Patient(patient_id, name, genre, birth_date, bed_number)
        func(*args, new_patient)
    return wrapper

def doctor_form(func):
    """Decorator to add a doctor"""
    def wrapper(*args):
        doctor_id = int(input('Doctor ID: '))
        name = input('Name: ')
        username = input('Username: ')
        password = input('Password: ')
        specialty = input('Specialty: ')
        new_doctor = a.Doctor(doctor_id, name, username, password, specialty)
        func(*args, new_doctor)
    return wrapper

def medicament_form(func):
    """Decorator to add a medicament"""
    def wrapper(*args):
        code = input('Code: ')
        name = input('Name: ')
        description = input('Description: ')
        new_medicament = a.Medicament(code, name, description)
        func(*args, new_medicament)
    return wrapper

def vital_signs_form(func):
    """Decorator to add vital signs"""
    def wrapper(*args):
        patient_id = int(input('Patient ID: '))

        for patient in args[0].patients:
            if patient.patient_id == patient_id:
                patient_id = patient
                break

        blood_pressure = input('Blood pressure: ')
        temperature = input('Temperature: ')
        oxygen_saturation = input('Oxygen saturation: ')
        heart_rate = input('Heart rate: ')
        new_vital_signs = a.VitalSigns(patient_id, blood_pressure, temperature, oxygen_saturation, heart_rate)
        func(*args, new_vital_signs)
    return wrapper

def exam_result_form(func):
    """Decorator to add an exam result"""
    def wrapper(*args):
        patient_id = int(input('Patient ID: '))

        for patient in args[0].patients:
            if patient.patient_id == patient_id:
                patient_id = patient
                break

        exam_id = input('Exam ID: ')
        exam_type = input('Exam type: ')
        result = input('Result: ')
        new_exam_result = a.ExamResult(patient_id, exam_id, exam_type, result)
        func(*args, new_exam_result)
    return wrapper

def note_form(func):
    """Decorator to add a note"""
    def wrapper(*args):
        patient_id = int(input('Patient ID: '))

        for patient in args[0].patients:
            if patient.patient_id == patient_id:
                patient_id = patient
                break

        note = input('Note: ')
        new_note = a.EvolutionNotes(patient_id, note)
        func(*args, new_note)
    return wrapper
