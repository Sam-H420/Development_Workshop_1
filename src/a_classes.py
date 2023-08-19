"""Aditional Classes"""

class Date:
    """Class representing a date"""

    def __init__(self, day, month, year):
        self.day = day
        self.month =  month
        self.year = year

    def __str__(self) -> str:
        return f'{self.day}/{self.month}/{self.year}'

class Patient:
    """Class representing a patient"""

    def __init__(self, patient_id, name, genre, birth_date):
        self.__patient_id = patient_id
        self.name = name
        self.genre = genre
        self.birth_date = birth_date

    @property
    def get_patient_id(self):
        """Returns the patient ID"""
        return self.__patient_id

    def __str__(self) -> str:
        return f'ID: {self.__patient_id}\nName: {self.name}\nGenre: {self.genre}\nBirth_date: {self.birth_date}\n'

class Medicament:
    """Class representing a medicament"""

    def __init__(self, medicament_id, name, prescription):
        self.medicament_id = medicament_id
        self.name = name
        self.__prescription = prescription

    def __str__(self):
        return f'\tID: {self.medicament_id}\n\tName: {self.name}\n\tPrescription: {self.__prescription}'

class VitalSigns():
    """Class representing the vital signs of a patient"""

    def __init__(self, patient, arterial_pressure, temperature, oxygen_saturation, breathing_frecuency):
        self.patient = patient
        self.arterial_pressure = arterial_pressure
        self.temperature = temperature
        self.oxygen_saturation = oxygen_saturation
        self.breathing_frecuency = breathing_frecuency

    def __str__(self) -> str:
        return f'\tArterial Pressure: {self.arterial_pressure}\n\tTemperature: {self.temperature}\n\tOxygen Saturation: {self.oxygen_saturation}\n\tBreathing frecuency: {self.breathing_frecuency}'

class ExamResult:
    """Class representing an exam result"""

    def __init__(self, patient, exam_id, exam_type, result):
        self.patient = patient
        self.exam_id = exam_id
        self.exam_type = exam_type
        self.__result = result

    @property
    def result(self):
        """Returns the result of the exam"""
        return self.__result

    @result.setter
    def result(self, new_result):
        self.__result = new_result

    def result_is_positive(self):
        """Returns the result in more understandable way"""

        if self.__result == 'p':
            return 'Positive'
        elif self.__result == 'n':
            return 'Negative'
        elif self.__result == 'u':
            return 'Unknown'
        else:
            return 'error getting result'

    def __str__(self) -> str:
        return f'\tExam ID: {self.exam_id}\n\tType: {self.exam_id}\n\t\t>: {self.result_is_positive}'

class Notes:
    """Class representing an evolution note"""
    def __init__(self, patient, note):
        self.patient = patient
        self.__note = note

    @property
    def note(self):
        """Returns the evolution note"""
        return self.__note

    @note.setter
    def note(self, edited_note):
        self.__note = edited_note

    def __str__(self) -> str:
        return f'{self.__note}'
