"""Aditional Classes"""

class Date:
    """Class representing a date"""

    def __init__(self, day, month, year):
        self.day = day
        self.month =  month
        self.year = year

    def __str__(self) -> str:
        return f'{self.day}/{self.month}/{self.year}'

class Doctor:
    """Class representing a doctor"""

    def __init__(self, doctor_id, name, username, password, specialty):
        self.__doctor_id = doctor_id
        self.__name = name
        self.__username = username
        self.__password = password
        self.__specialty = specialty

    @property
    def doctor_id(self):
        """Returns the doctor ID"""
        return self.__doctor_id

    @property
    def name(self):
        """Returns the name"""
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def username(self):
        """Returns the username"""
        return self.__username

    @username.setter
    def username(self, new_username):
        self.__username = new_username

    @property
    def password(self):
        """Returns the password"""
        return self.__password

    @property
    def specialty(self):
        """Returns the specialty"""
        return self.__specialty

    @specialty.setter
    def specialty(self, new_specialty):
        self.__specialty = new_specialty

    def __repr__(self) -> str:
        return f'\n\tID: {self.__doctor_id}\n\tName: {self.__name}\n\tUsername: {self.__username}\n\tSpecialty: {self.__specialty}\n'

class Patient:
    """Class representing a patient"""

    __is_critic = False
    __is_out = False

    def __init__(self, patient_id, name, genre, birth_date, bed_number = None):
        self.__patient_id = patient_id
        self.name = name
        self.genre = genre
        self.birth_date = birth_date
        self.__bed_number = bed_number
        if bed_number is not None:
            self.__is_out = False
            self.__is_critic = True
    @property
    def bed_number(self):
        """Returns the bed number if exists"""
        return self.__bed_number

    @bed_number.setter
    def bed_number(self, new_bed_number):
        if new_bed_number is not None:
            self.is_critic = True
        self.__bed_number = new_bed_number

    @property
    def is_critic(self):
        """Returns if the patient is critic"""
        return self.__is_critic

    @property
    def is_out(self):
        """Returns if the patient is out"""
        return self.__is_out

    @is_out.setter
    def is_out(self, new_is_out):
        self.__is_out = new_is_out

    if __is_out:
        __is_critic = False
        __bed_number = None

    @property
    def patient_id(self):
        """Returns the patient ID"""
        return self.__patient_id

    def __str__(self) -> str:
        if self.__is_critic:
            return f'ID: {self.__patient_id}\nName: {self.name}\nGenre: {self.genre}\nBirth_date: {self.birth_date}\nBed_number: {self.__bed_number}\n'
        else:
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
        return f'\n\tExam ID: {self.exam_id}\n\tType: {self.exam_type}\n\t>: {self.__result}\n'

class DiagnosticImage:
    """Class representing a diagnostic image"""

    def __init__(self, patient, image_id, image_type):
        self.patient = patient
        self.image_id = image_id
        self.image_type = image_type

    def __repr__(self) -> str:
        return f'\n\tImage ID: {self.image_id}\n\tType: {self.image_type}\n'

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

    def __repr__(self) -> str:
        return f'\n{self.__note}\n'
