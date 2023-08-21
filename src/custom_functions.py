"""This module contains custom functions used in the App"""

import a_classes as a
from patient_history import PatientHistory

# define a decorator to add a date
def date_form():
    """Function to add a date to a class"""
    day = int(input('Day: '))
    month = int(input('Month: '))
    year = int(input('Year: '))
    date = a.Date(day, month, year)
    return date

# define patient_form function
def patient_form():
    """function to add a patient"""
    patient_id = input('ID: ')
    name = input('Name: ')
    genre = input('Genre: ')
    birth_date = date_form()
    bed_number = input('Bed number: ')
    patient = a.Patient(patient_id, name, genre, birth_date, bed_number)
    return patient

# define doctor_form function
def doctor_form():
    """function to add a doctor"""
    doctor_id = int(input('ID: '))
    name = input('Name: ')
    username = input('Username: ')
    password = input('Password: ')
    specialty = input('Specialty: ')
    doctor = a.Doctor(doctor_id, name, username, password, specialty)
    return doctor

# define vital_signs_form function
def vital_signs_form(patient):
    """function to add vital signs"""
    blood_pressure = input('Blood pressure: ')
    temperature = input('Temperature: ')
    oxygen_saturation = input('Oxygen saturation: ')
    heart_rate = input('Heart rate: ')
    vital_signs = a.VitalSigns(patient, blood_pressure, temperature, oxygen_saturation, heart_rate)
    return vital_signs

# define exam_result_form function
def exam_result_form(patient):
    """function to add an exam result"""
    exam_id = int(input('ID: '))
    name = input('Name: ')
    result = input('Result: ')
    exam_result = a.ExamResult(patient, exam_id, name, result)
    return exam_result

# define medicament_form function
def medicament_form():
    """function to add a medicament"""
    medicament_id = int(input('ID: '))
    name = input('Name: ')
    prescription = input('Prescription: ')
    medicament = a.Medicament(medicament_id, name, prescription)
    return medicament

# define evolution_note_form function
def evolution_note_form(patient):
    """function to add an evolution note"""
    note = input('Note: ')
    evolution_note = a.EvolutionNotes(patient, note)
    return evolution_note

# define patient_history_form function
def patient_history_form():
    """function to add a patient history"""
    patient = patient_form()
    vital_signs = vital_signs_form(patient)
    exam_result = (exam_result_form(patient))
    medicament = (medicament_form())
    evolution_note = (evolution_note_form(patient))
    patient_history = PatientHistory(patient, vital_signs, exam_result, medicament, evolution_note)
    return patient_history
