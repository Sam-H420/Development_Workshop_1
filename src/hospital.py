"""Main information cluster"""

import custom_functions as cf
import a_classes as a
from patient_history import PatientHistory

class Hospital:
    """Class representing a hospital"""

    def __init__(self, name, patients, doctors):
        self.name = name
        self.__patients = patients
        self.__doctors = doctors

    @property
    def patients(self):
        """Returns all the patients"""
        return self.__patients

    @property
    def doctors(self):
        """Returns all the doctors"""
        return self.__doctors

    @cf.patient_form
    def _add_patient(self, *new_patient):
        """Adds a new patient"""
        self.__patients.append(new_patient)

    @cf.doctor_form
    def _add_doctor(self, new_doctor):
        """Adds a new doctor"""
        self.__doctors.append(new_doctor)

    def _get_patient(self, patient_id):
        """Returns a patient by its id"""
        find = False
        index = 0
        for patient in self.__patients:
            if patient.patient_id == patient_id:
                find = True
                index = self.__patients.index(patient)
            else:
                find = False
        if find:
            return self.__patients[index]
        else:
            return None

    def _get_stats(self):
        """Returns the stats of the hospital"""
        return f'Patients: {len(self.__patients)}\nDoctors: {len(self.__doctors)}'

    def patient_menu(self, patient):
        """Patient menu"""
        print(f'Welcome {patient.name}\n1. See patient history\n2. See vital signs\n3. See exam results\n4. See medicaments\n5. See evolution notes\n6. Exit\n')
        option = input('Select an option: ')
        if option == '1':
            print(patient.patient_history)
        elif option == '2':
            print(patient.patient_history.vital_signs)
        elif option == '3':
            print(patient.patient_history.exam_results)
        elif option == '4':
            print(patient.patient_history.medicaments)
        elif option == '5':
            print(patient.patient_history.notes)
        elif option == '6':
            pass
        else:
            print('Invalid option')
            self.patient_menu(patient)

    def _menu(self):
        """Main menu of the hospital"""
        print(f'Welcome to {self.name}\n1. Search patient\n2. Register patient\n3. Stats\n4. Exit\n')
        option = input('Select an option: ')
        if option == '1':
            search_id = input('Enter the patient id: ')
            result = self._get_patient(search_id)
            self.patient_menu(result)
        elif option == '2':
            self._add_patient()
        elif option == '3':
            print(self._get_stats())
        elif option == '4':
            pass
        else:
            print('Invalid option')
            self._menu()
