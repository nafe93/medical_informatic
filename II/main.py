import datetime
import glob
import os


class HL7:

    def __init__(self, path):
        self.path = path
        self.book = ''
        self.sur_name = ''
        self.name = ''
        self.middle_name = ''
        self.suffiks = ''
        self.data_burn = ''
        self.year_old = ''

    def read_the_file(self):
        try:
            with open(self.path, 'r') as file:
                self.book = file.read()
        except IOError:
            return "We don't have this file"

    def view_text(self):
        return self.book

    def find_patient_name(self):
        pid = self.book.split('PID')[1]
        full_patient_name_str = pid.split('|')[5]
        full_patient_name_list = full_patient_name_str.split('^')
        self.sur_name, self.sur_name, self.middle_name, self.suffiks = full_patient_name_list

    def view_patient_information(self):
        print(f"SurName: {self.sur_name}", f"Name: {self.sur_name}", f"middle name: {self.middle_name}",
              f"Suffiks: {self.suffiks}", f"Year burn: {self.data_burn}", f"Old year: {self.year_old}", sep='\n')

    def find_patient_age(self):
        pid = self.book.split('PID')[1]
        patient_data_burn = pid.split('|')[7]
        patient_data_burn_list = datetime.datetime.strptime(patient_data_burn, '%Y%m%d').date()
        self.data_burn = patient_data_burn_list

    def find_current_age(self):
        current_year = int(datetime.datetime.now().year)
        current_patient_year = current_year - int(self.data_burn.year)
        self.year_old = current_patient_year

    def save_to_set(self):
        return [self.sur_name,
                self.name,
                self.middle_name,
                self.suffiks,
                self.data_burn,
                self.year_old
                ]


all_patient = list()

directory = glob.glob("./HW2/Clinical_HL7_Samples/*.out")
for i in directory:
    hl7 = HL7(i)
    hl7.read_the_file()
    hl7.find_patient_age()
    hl7.find_patient_name()
    hl7.find_current_age()
    

print(f"unique element: {len(all_patient)}")


for i in all_patient:
    i = list(i)


print(*all_patient, sep='\n')
# print(*sorted(all_patient, ), sep='\n')

