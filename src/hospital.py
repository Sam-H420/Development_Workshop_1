"""Main information cluster"""

import custom_functions as cf

class Hospital:
    """Class representing a hospital"""

    def __init__(self, name, patient_histories, doctors):
        self.name = name
        self.__patient_histories = patient_histories
        self.__doctors = doctors

    @property
    def patients(self):
        """Returns all the patients"""
        return self.__patient_histories.patient

    @property
    def doctors(self):
        """Returns all the doctors"""
        return self.__doctors

    def _add_patient(self, new_patient_history):
        """Adds a new patient"""
        self.__patient_histories.append(new_patient_history)

    def _add_doctor(self, new_doctor):
        """Adds a new doctor"""
        self.__doctors.append(new_doctor)

    def _get_patient(self, patient_id):
        """Returns a patient by its id"""
        index = 0
        find = False
        for patient in self.__patient_histories:
            if patient.patient_id == patient_id:
                find = True
                index = self.__patient_histories.index(patient)
                break

        if find:
            return int(index)
        else:
            print('Patient not found\n')
            self._menu()
        return None

    def _get_stats(self):
        """Returns the stats of the hospital"""
        return f'Patients: {len(self.__patient_histories)}\nDoctors: {len(self.__doctors)}'

    def _patient_menu(self, patient_index):
        """Patient menu"""
        name = self.__patient_histories[patient_index].name
        if self.__patient_histories[patient_index].bed_number is not None:
            name = self.__patient_histories[patient_index].name + ' (Critic)'
        print(f'\n{name}\n\n0. History resume\n1. All exams\n2. All notes\n3. Add note\n4. Add exam result\n5. Add medicament\n6. Exit\n')
        option = input('Select an option: ')

        if option == '0':
            print(self.__patient_histories[patient_index])
            self._patient_menu(patient_index)
        elif option == '1':
            print(self.__patient_histories[patient_index].exam_results)
            self._patient_menu(patient_index)
        elif option == '2':
            print(self.__patient_histories[patient_index].notes)
            self._patient_menu(patient_index)
        elif option == '3':
            new_note = cf.evolution_note_form(self.__patient_histories[patient_index])
            self.__patient_histories[patient_index].add_notes(new_note)
            self._patient_menu(patient_index)
        elif option == '4':
            new_exam_result = cf.exam_result_form(self.__patient_histories[patient_index])
            self.__patient_histories[patient_index].add_exam_result(new_exam_result)
            self._patient_menu(patient_index)
        elif option == '5':
            new_medicament = cf.medicament_form()
            self.__patient_histories[patient_index].add_medicament(new_medicament)
            self._patient_menu(patient_index)
        elif option == '6':
            self._menu()
        else:
            print('Invalid option')
            self._patient_menu(patient_index)

    def _menu(self):
        """Main menu of the hospital"""
        print(f'Welcome to {self.name}\n1. Search patient\n2. Register patient\n3. Stats\n4. Exit\n')
        option = input('Select an option: ')
        if option == '1':
            search_id = input('Enter the patient id: ')
            result = self._get_patient(search_id)
            self._patient_menu(result)
        elif option == '2':
            new_patient = cf.patient_history_form()
            self._add_patient(new_patient)
            self._menu()
        elif option == '3':
            print(self._get_stats())
            self._menu()
        elif option == '4':
            pass
        else:
            print('Invalid option')
            self._menu()
