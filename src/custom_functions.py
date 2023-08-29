"""This module contains custom functions used in the App"""

import a_classes as a
from patient_history import PatientHistory

# define a decorator to add a date
def date_form():
    """Function to add a date to a class"""
    date = input('Date (dd/mm/yyyy): ')
    day = int(date[0:2])
    month = int(date[3:5])
    year = int(date[6:10])
    date = a.Date(day, month, year)
    return date

# define patient_form function
def patient_form():
    """function to add a patient"""
    patient_id = input('ID: ')
    name = input('Name: ')
    genre = input('Genre: ')
    birth_date = date_form()
    is_critic = input('\nIs critic? (Patient is not critic by default) (y/n): ')
    if is_critic == 'y':
        in_date = date_form()
        bed_number = input('Bed number: ')
        patient = a.Patient(patient_id, name, genre, birth_date, bed_number, in_date)
    elif is_critic == 'n':
        patient = a.Patient(patient_id, name, genre, birth_date)
    else:
        print('Invalid option')
        patient = a.Patient(patient_id, name, genre, birth_date)
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
    exam_id = int(input(' Exam ID: '))
    name = input('Name: ')
    result = input('Result: ')
    exam_result = a.ExamResult(patient, exam_id, name, result)
    return exam_result

# define diagnostic_image_form function
def diagnostic_image_form(patient):
    """function to add a diagnostic image"""
    image_id = int(input('Image ID: '))
    name = input('Image type: ')
    diagnostic_image = a.DiagnosticImage(patient, image_id, name)
    return diagnostic_image

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
    print('\nPatient data:')
    patient = patient_form()
    print('\nVital signs:')
    vital_signs = vital_signs_form(patient)
    print('\nExam result:')
    exam_result = exam_result_form(patient)
    print('\nDiagnostic image:')
    diagnostic_image = diagnostic_image_form(patient)
    print('\nMedicament:')
    medicament = medicament_form()
    print('\nEvolution note:')
    evolution_note = evolution_note_form(patient)
    patient_history = PatientHistory(patient, vital_signs, [exam_result], [diagnostic_image], [medicament], [evolution_note])
    return patient_history
