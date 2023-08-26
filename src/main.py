"""Main App module"""

import a_classes as a
from patient_history import PatientHistory
from hospital import Hospital

# create 2 random birth dates
birth_date_1 = a.Date(1, 1, 2000)
birth_date_2 = a.Date(1, 1, 2000)

# create 2 random patients
patient_1 = a.Patient('12345678A', 'John Doe', 'M', birth_date_1)
patient_2 = a.Patient('87654321B', 'Jane Doe', 'F', birth_date_2, '2B')

# create 2 random doctors with doctor_id, name, username, password, specialty
doctor_1 = a.Doctor('12345678A', 'John Doe', 'jdoe', '1234', 'Cardiology')
doctor_2 = a.Doctor('87654321B', 'Jane Doe', 'jadoe', '4321', 'Neurology')

# create 2 random vital signs with patient, arterial_pressure, temperature, oxygen_saturation, breathing_frecuency
vital_signs_1 = a.VitalSigns(patient_1, '120/80', '36.5', '98', '16')
vital_signs_2 = a.VitalSigns(patient_2, '120/80', '36.5', '98', '16')

# create 4 random exam results with patient, exam_id, name, result
exam_result_1 = a.ExamResult(patient_1, '123456789', 'Blood test', 'Normal')
exam_result_2 = a.ExamResult(patient_2, '987654321', 'Blood test', 'Normal')
exam_result_3 = a.ExamResult(patient_1, '123456789', 'Urine test', 'Normal')
exam_result_4 = a.ExamResult(patient_2, '987654321', 'Urine test', 'Normal')

# create 2 random diagnostic images with patient, image_id, name
diagnostic_image_1 = a.DiagnosticImage(patient_1, '123456789', 'X-Ray')
diagnostic_image_2 = a.DiagnosticImage(patient_2, '987654321', 'X-Ray')

# create 2 random medicaments with medicament_id, name, prescription
medicament_1 = a.Medicament('123456789', 'Paracetamol', '1-1-1')
medicament_2 = a.Medicament('987654321', 'Ibuprofen', '1-1-1')

# create 4 random evolution notes with patient, note
evolution_note_1 = a.EvolutionNotes(patient_1, 'Patient is feeling well')
evolution_note_2 = a.EvolutionNotes(patient_2, 'Patient is feeling well')
evolution_note_3 = a.EvolutionNotes(patient_1, 'Patient is feeling bad')
evolution_note_4 = a.EvolutionNotes(patient_2, 'Patient is feeling bad')

# create 2 random patient histories with patient, vital_signs, exam_result, medicament, evolution_note
patient_history_1 = PatientHistory(patient_1, vital_signs_1, [exam_result_1,exam_result_3], [diagnostic_image_1,diagnostic_image_2], [medicament_1,medicament_2], [evolution_note_1, evolution_note_3])
patient_history_2 = PatientHistory(patient_2, vital_signs_2, [exam_result_2,exam_result_4], [diagnostic_image_1,diagnostic_image_2], [medicament_1,medicament_2], [evolution_note_2, evolution_note_4])

# create a random hospital with name, patient_histories, doctors
hospital = Hospital('Hospital', [patient_history_1, patient_history_2], [doctor_1, doctor_2])

hospital.login()
