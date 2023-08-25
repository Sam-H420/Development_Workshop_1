"""Class PatientHistory"""

import a_classes as a

class PatientHistory(a.Patient):
    """Class representing the clinical history of a patient"""

    def __init__(self, patient, vital_signs, exam_results, diagnostic_images, medicaments, evolution_notes):
        super().__init__(patient.patient_id, patient.name, patient.genre, patient.birth_date,)
        self.__vital_signs = vital_signs
        self.__exam_results = exam_results
        self.__diagnostic_images = diagnostic_images
        self.__medicaments = medicaments
        self.__evolution_notes = evolution_notes

    @property
    def notes(self):
        """Returns all the notes of the clinical history"""
        return self.__evolution_notes

    @property
    def exam_results(self):
        """Returns all the exam results of the clinical history"""
        return self.__exam_results

    @property
    def diagnostic_images(self):
        """Returns all the diagnostic images of the clinical history"""
        return self.__diagnostic_images

    @property
    def vital_signs(self):
        """Returns the vital signs of the clinical history"""
        return self.__vital_signs

    @vital_signs.setter
    def vital_signs(self, new_vital_signs):
        self.__vital_signs = new_vital_signs

    @property
    def medicaments(self):
        """Returns the medicaments of the clinical history"""
        return self.__medicaments

    @property
    def _last_note(self):
        """Returns the last note of the clinical history"""
        return self.__evolution_notes[len(self.__evolution_notes) - 1]

    @property
    def _last_exam_result(self):
        """Returns the last exam result of the clinical history"""
        return self.__exam_results[len(self.__exam_results) - 1]

    @property
    def _last_diagnostic_image(self):
        """Returns the last diagnostic image of the clinical history"""
        return self.__diagnostic_images[len(self.__diagnostic_images) - 1]

    def add_notes(self, new_note):
        """Adds a new note to the clinical history"""
        self.__evolution_notes.append(new_note)

    def add_medicament(self, new_medicament):
        """Adds a new medicament to the clinical history"""
        self.__medicaments.append(new_medicament)

    def add_exam_result(self, new_exam_result):
        """Adds a new exam result to the clinical history"""
        self.__exam_results.append(new_exam_result)

    def add_diagnostic_image(self, new_diagnostic_image):
        """Adds a new diagnostic image to the clinical history"""
        self.__diagnostic_images.append(new_diagnostic_image)

    def __str__(self) -> str:
        return f'{super().__str__()}\nVital Signs:\n{self.__vital_signs}\n\nExam Results:\n{self._last_exam_result}\n\nDiagnostic Images:\n{self._last_diagnostic_image}\n\nMedicaments:\n{self.__medicaments}\n\nNotes:\n{self._last_note}'
