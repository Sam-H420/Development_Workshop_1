"""Main information cluster"""

import custom_functions as cf

# cronic diseases list
cronic_diseases = [
    'Diabetes',
    'Asthma',
    'Cancer',
    'Arthritis',
    'Obesity',
    'Alzheimer'
]

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

        ocupation = 0
        for patient in self.__patient_histories:
            if patient.bed_number is not None:
                ocupation += 1

        prescription_per_patient = 0
        for patient in self.__patient_histories:
            prescription_per_patient += len(patient.medicaments)
        prescription_per_patient = prescription_per_patient/len(self.__patient_histories)

        cronic_patients = 0
        for patient in self.__patient_histories:
            for exam in patient.exam_results:
                if exam.result == 'Positive' and exam.name in cronic_diseases:
                    cronic_patients += 1
                    break

        outside_patients = 0
        for patient in self.__patient_histories:
            if patient.is_out:
                outside_patients += 1

        return f'Admited Patients: {len(self.__patient_histories)}\nOccupation: {(ocupation/300)*100}%\nOut patients: {outside_patients}\nPescriptions per patient (Average): {prescription_per_patient}\nCronic patients: {cronic_patients}\n'

    def _patient_menu(self, patient_index):
        """Patient menu"""
        name = self.__patient_histories[patient_index].name
        if self.__patient_histories[patient_index].bed_number is not None:
            name = self.__patient_histories[patient_index].name + ' (Critic)'
        print(f'\nPatent: {name}\n\n0. History resume\n1. All exams\n2. All images\n3. All notes\n4. Add note\n5. Add exam result\n6. Add diagnostic image\n7. Add medicament\n8. Check in\n9. Check out\n10. Exit\n')
        option = input('Select an option: ')

        if option == '0':
            print(self.__patient_histories[patient_index])
            self._patient_menu(patient_index)
        elif option == '1':
            print(self.__patient_histories[patient_index].exam_results)
            self._patient_menu(patient_index)
        elif option == '2':
            print(self.__patient_histories[patient_index].diagnostic_images)
            self._patient_menu(patient_index)
        elif option == '3':
            print(self.__patient_histories[patient_index].notes)
            self._patient_menu(patient_index)
        elif option == '4':
            new_note = cf.evolution_note_form(self.__patient_histories[patient_index])
            self.__patient_histories[patient_index].add_notes(new_note)
            self._patient_menu(patient_index)
        elif option == '5':
            new_exam_result = cf.exam_result_form(self.__patient_histories[patient_index])
            self.__patient_histories[patient_index].add_exam_result(new_exam_result)
            self._patient_menu(patient_index)
        elif option == '6':
            new_diagnostic_image = cf.diagnostic_image_form(self.__patient_histories[patient_index])
            self.__patient_histories[patient_index].add_diagnostic_image(new_diagnostic_image)
            self._patient_menu(patient_index)
        elif option == '7':
            new_medicament = cf.medicament_form()
            self.__patient_histories[patient_index].add_medicament(new_medicament)
            self._patient_menu(patient_index)
        elif option == '8':
            if self.__patient_histories[patient_index].is_out:    
                self.__patient_histories[patient_index].is_out = False
                self.__patient_histories[patient_index].in_date = cf.date_form()
                self.__patient_histories[patient_index].bed_number = input('Bed number: ')
                print('Patient checked in successfully')
                self._patient_menu(patient_index)
            else:
                print('Patient is already checked in')
                self._patient_menu(patient_index)
        elif option == '9':
            if self.__patient_histories[patient_index].is_out:
                print('Patient is already out')
                self._patient_menu(patient_index)
            else:
                self.__patient_histories[patient_index].is_out = True
                self.__patient_histories[patient_index].out_date = cf.date_form()
                self.__patient_histories[patient_index].bed_number = None
                print('Patient checked out successfully')
                self._patient_menu(patient_index)
        elif option == '10':
            self._menu()
        else:
            print('Invalid option')
            self._patient_menu(patient_index)

    def _menu(self):
        """Main menu of the hospital"""
        print(f'\nWelcome to {self.name}\n1. Search patient\n2. Register patient\n3. Stats\n4. Exit\n')
        option = input('Select an option: ')
        if option == '1':
            search_id = input('Enter the patient id: ')
            result = self._get_patient(search_id)
            self._patient_menu(result)
        elif option == '2':
            new_patient = cf.patient_history_form()
            self._add_patient(new_patient)
            print('Patient added successfully')
            self._menu()
        elif option == '3':
            print(self._get_stats())
            self._menu()
        elif option == '4':
            pass
        else:
            print('Invalid option')
            self._menu()

    # define login function
    def login(self):
        """Login function"""
        print('Welcome to the hospital system\n')
        username = input('Username: ')
        password = input('Password: ')
        find = False
        for doctor in self.__doctors:
            if doctor.username == username and doctor.password == password:
                find = True
                self._menu()
                break
        if not find:
            print('Invalid credentials\nWould you like to register instead? (y/n/c)')
            option = input('Select an option: ')
            if option == 'y':
                new_doctor = cf.doctor_form()
                self._add_doctor(new_doctor)
                self.login()
            elif option == 'n':
                self.login()
            elif option == 'c':
                pass
