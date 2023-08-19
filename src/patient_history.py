"""Class PatientHistory"""

import a_classes as a

class PatientHistory(a.Patient):
    """Class representing the clinical history of a patient"""
    
    def __init__(self, patient, vital_signs, exam_results, medicaments, evolution_notes):
        super().__init__(patient.patient_id, patient.name, patient.genre, patient.birth_date)
        self.vital_signs = vital_signs
        self.exam_results = exam_results
        self.medicaments = medicaments
        self.evolution_notes = evolution_notes
