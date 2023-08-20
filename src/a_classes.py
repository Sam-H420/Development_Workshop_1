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

    def __init__(self, patient_id, name, genre, birth_date, bed_number):
        self.__patient_id = patient_id
        self.name = name
        self.genre = genre
        self.birth_date = birth_date
        self.__bed_number = bed_number

    @property
    def patient_id(self):
        """Returns the patient ID"""
        return self.__patient_id

    @property
    def bed_number(self):
        """Returns the bed number"""
        return self.__bed_number

    @bed_number.setter
    def bed_number(self, new_bed_number):
        self.__bed_number = new_bed_number

    def __str__(self) -> str:
        return f'ID: {self.__patient_id}\nName: {self.name}\nGenre: {self.genre}\nBirth_date: {self.birth_date}\n'

class Medicament:
    """Class representing a medicament"""

    def __init__(self, medicament_id, name, prescription):
        self.medicament_id = medicament_id
        self.name = name
        self.__prescription = prescription

    def __repr__(self) -> str:
        return f'\n\tID: {self.medicament_id}\n\tName: {self.name}\n\tPrescription: {self.__prescription}\n'

class VitalSigns():
    """Class representing the vital signs of a patient"""

    def __init__(self, patient, arterial_pressure, temperature, oxygen_saturation, breathing_frecuency):
        self.patient = patient
        self.arterial_pressure = arterial_pressure
        self.temperature = temperature
        self.oxygen_saturation = oxygen_saturation
        self.breathing_frecuency = breathing_frecuency

    def __repr__(self) -> str:
        return f'\n\tArterial Pressure: {self.arterial_pressure}\n\tTemperature: {self.temperature}\n\tOxygen Saturation: {self.oxygen_saturation}\n\tBreathing frecuency: {self.breathing_frecuency}\n'

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

    def __repr__(self) -> str:
        return f'\tExam ID: {self.exam_id}\n\tType: {self.exam_type}\n\t>: {self.__result}'

class EvolutionNotes:
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
