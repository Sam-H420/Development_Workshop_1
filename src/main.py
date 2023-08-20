"""Main App module"""

import a_classes as a
from patient_history import PatientHistory

jose_birth_date = a.Date(15, 10, 1990)
patient_1 = a.Patient(1, 'Jose', 'M', jose_birth_date, 1)
medicaments_1 = [a.Medicament('1515', 'Acetaminofem', '1 pill every 12h'), a.Medicament('1516', 'Ibuprofen', '1 pill every 8h')]
jose_vital_signs = [a.VitalSigns(patient_1, '120/80', '36.5', '98%', '16')]
jose_exam_results = [a.ExamResult(patient_1, 1, 'Cancer Test', 'Negative'), a.ExamResult(patient_1, 2, 'Pregnancy test', 'Unknown')]
jose_evolution_notes = [a.EvolutionNotes(patient_1, 'Patient is feeling better'), a.EvolutionNotes(patient_1, 'Patient is feeling worse')]

patient_history_1 = PatientHistory(patient_1, jose_vital_signs, jose_exam_results, medicaments_1, jose_evolution_notes)
print(patient_history_1)
