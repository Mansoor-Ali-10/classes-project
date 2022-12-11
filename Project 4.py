# Hello World

from tabulate import tabulate
class Doctor():
    def formatDrInfo(DocInfo):
      formatted = '_'.join(str(x) for x in DocInfo)
      return formatted

    def formatWholeFile(editDoctorInfo):
      for each_doc in editDoctorInfo:
        formatted_file = '_'.join(str(x) for x in each_doc)
        return formatted_file

    def enterDrInfo():
        doc_id = int(input("Enter the doctor's ID: "))
        doc_name = input("Enter the doctor's name: ")
        doc_spec = input("Enter the doctor's specialty: ")
        doc_time = input("Enter the doctor's timing (e.g., 7am-10pm): ")
        doc_qual = input("Enter the doctor's qualification: ")
        doc_room = input("Enter the doctor's room number: ")
        # Put into a list
        doc_info = [doc_id, doc_name, doc_spec, doc_time, doc_room]
        return doc_info
    
    def readDoctorsFile():
      doc_file = open('/content/doctors.txt', 'r')
      doctor_data = doc_file.readlines()
      doc_data_list = []
      for line in doctor_data:
        doc_list = line.strip('\n').split('_')
        doc_data_list.append(doc_list)
      return doc_data_list

    def searchDoctorByld(readDoctorsFile):
      doc_id = input('Enter the doctor ID: ')
      counter = 0
      for line in readDoctorsFile:
        if doc_id in line:
          table = [['ID','Name','Specialty','Timing','Qualification','Room Number']]
          table.append(line)
          print(tabulate(table, headers = 'firstrow'))
          print('\n')
          print('Back to the previous Menu\n')
        else:
          counter += 1
      if counter == len(readDoctorsFile):
        print("Can't find the doctor with the same ID on the system")
        print('\n')

    def searchDoctorByName(readDoctorsFile):
      doc_name = input('Enter the doctor name: ')
      counter = 0
      for line in readDoctorsFile:
        if doc_name in line:
          table = [['ID','Name','Specialty','Timing','Qualification','Room Number']]
          table.append(line)
          print(tabulate(table, headers = 'firstrow'))
          print('\n')
          print('Back to the previous Menu\n')
        else:
          counter += 1
      if counter == len(readDoctorsFile):
        print("Can't find the doctor with the same name on the system")
        print('\n')

    def displayDoctorInfo(readDoctorsFile):
      for x in readDoctorsFile:
        print(x)

    def editDoctorInfo(request_id):
      doc_file = open('/content/doctors.txt', 'r')
      doctor_data = doc_file.readlines()
      for line in doctor_data:
        if request_id in line:
          doc_id = request_id
          doc_name = input("Enter the doctor's name: ")
          doc_spec = input("Enter the doctor's specialty: ")
          doc_time = input("Enter the doctor's timing (e.g., 7am-10pm): ")
          doc_qual = input("Enter the doctor's qualification: ")
          doc_room = input("Enter the doctor's room number: ")
      doc_info = [doc_id, doc_name, doc_spec, doc_time, doc_room]
      return doc_info

    def displayDoctorsList(readDoctorsFile):
      print(tabulate(readDoctorsFile, headers = 'firstrow'))

    def writeListOfDoctorsToFile(formatDrInfo):
      with open('/content/doctors.txt', 'r') as doc_file:
        lines = doc_file.readlines()
        doc_file2 = open('doctors.txt', 'w')
        for line in lines:
          if request_id not in line:
            doc_file2.write(line)
          elif request_id in line:
            doc_file2.write(formatDrInfo)
            doc_file2.write('\n')
        doc_file2.close()
        # Writes the list of doctors to the doctors.txt file after formatting it correctly

    def addDrToFile(formatDrInfo):
      doc_file = open('/content/doctors.txt', 'a')
      doc_file.write('\n')
      doc_file.write(formatDrInfo)
      doc_file.close()
        # Writes doctors to the doctors.txt file after formatting it correctly

class Facility():
    def displayFacilities():
      fac_file = open('/content/facilities.txt', 'r')
      fac_data = fac_file.readlines()
      fac_data_list = []
      for line in fac_data:
        fac_list = line.strip('\n')
        print(fac_list)

    def addFacility():
      fac_name = input('Enter Facility Name: ')
      fac_file = open('/content/facilities.txt', 'a')
      fac_file.write('\n')
      fac_file.write(fac_name)
      fac_file.close()
      # Adds and writes the facility name to the file

    def writeListOffacilitiesToFile(self):
      pass
      # Writes the facilities list to facilities.txt

class Laboratory():
    def displayLabsList():
      with open('/content/laboratories.txt', 'r') as lab_file:
        data = lab_file.read()
        data = data.replace('Facility', 'Lab')
        data = data.replace('_', '      ')

        li = list(data.split('\n'))

        for x in li:
          print('\n')
          print(x)

    def addLabToFile():
      lab_num = input('Enter Laboratory Facility: ')
      print('\n')
      lab_cost = input("Enter Laboratory Cost: ")

      lab_add = lab_num + '_' + lab_cost
      facility_add = lab_add.replace('Lab', 'Facility')

      with open('/content/laboratories.txt', 'a') as lab_file:
        lab_file.write('\n')
        lab_file.write(facility_add)
        lab_file.close()

class Patient():
    def formatPatientInfo(PatInfo):
      formatted = '_'.join(str(x) for x in PatInfo)
      return formatted

    def readPatientsFile():
      pat_file = open('/content/patients.txt', 'r')
      patient_data = pat_file.readlines()
      pat_data_list = []
      for line in patient_data:
        pat_list = line.strip('\n').split('_')
        pat_data_list.append(pat_list)
      return pat_data_list

    def searchPatientByld(readPatientsFile):
      pat_id = input('Enter the patient ID: ')
      counter = 0
      for line in readPatientsFile:
        if pat_id in line:
          table = [['ID','Name','Disese','Gender','Age']]
          table.append(line)
          print(tabulate(table, headers = 'firstrow'))
          print('\n')
          print('Back to the previous Menu\n')
        else:
          counter += 1
      if counter == len(readPatientsFile):
        print("Can't find the patient with the same ID on the system")
        print('\n')

    def displayPatientInfo(readPatientsFile):
      for x in readPatientsFile:
        print(x)

    def displayPatientsList(readPatientsFile):
      print(tabulate(readPatientsFile, headers = 'firstrow'))

    def enterPatientInfo():
      pat_id = int(input("Enter the patient's ID: "))
      pat_name = input("Enter the patient's name: ")
      pat_disease = input("Enter the patient's disease: ")
      pat_gender = input("Enter the patient's gender: ")
      pat_age = input("Enter the patient's age: ")
      # Put into a list
      pat_info = [pat_id, pat_name, pat_disease, pat_gender, pat_age]
      return pat_info
        # Asks the user to enter the patient info 

    def editPatientInfo(request_id):
      pat_file = open('/content/patients.txt', 'r')
      patient_data = pat_file.readlines()
      for line in patient_data:
        if request_id in line:
          pat_id = request_id
          pat_name = input("Enter the patient's name: ")
          pat_disease = input("Enter the patient's disease: ")
          pat_gender = input("Enter the patient's gender: ")
          pat_age = input("Enter the patient's age: ")
      pat_info = [pat_id, pat_name, pat_disease, pat_gender, pat_age]
      return pat_info
        # Asks the user to edit patient information

    def writeListOfPatientsToFile(formatPatientInfo):
      with open('/content/patients.txt', 'r') as pat_file:
        lines = pat_file.readlines()
      pat_file2 = open('patients.txt', 'w')
      for line in lines:
        if request_id not in line:
          pat_file2.write(line)
        elif request_id in line:
          pat_file2.write(formatPatientInfo)
          pat_file2.write('\n')
      pat_file2.close()
      # Writes a list of patients into the patients.txt file

    def addPatientToFile(formatPatientsInfo):
      pat_file = open('/content/patients.txt', 'a')
      pat_file.write('\n')
      pat_file.write(formatPatientsInfo)
      pat_file.close()
        # Adds a new patient to the file

class Management():
    def DisplayMenu():
      pass


selection = 5
while not (selection == 0):
  print('Welcome to Alberta Hospital (AH) Management System')
  print("Select from the following options, or select 0 to stop: ")
  print("""
  1 - Doctors
  2 - Facilities
  3 - Laboratories
  4 - Patients\n""")
  selection = int(input("\nSelection: "))
  print('\n')
  if selection == 0:
      break
  # To break out of while loop

  elif selection == 1:
    selection_doc = 7
    while not (selection_doc == 6):
      print("""Doctors Menu:
  1 - Display Doctors List
  2 - Search for doctor by ID
  3 - Search for doctor by name
  4 - Add doctor
  5 - Edit doctor info
  6 - Back to the Main Menu""")
      selection_doc = int(input("\nSelection: "))
      print('\n')

      if selection_doc == 1:
        doc_data_list = Doctor.readDoctorsFile()
        Doctor.displayDoctorsList(doc_data_list)
        print('\n')

      elif selection_doc == 2:
        doc_data_list = Doctor.readDoctorsFile()          
        Doctor.searchDoctorByld(doc_data_list)
        print('\n')      

      elif selection_doc == 3:
        doc_data_list = Doctor.readDoctorsFile()
        Doctor.searchDoctorByName(doc_data_list)
        print('\n')

      elif selection_doc == 4:
        doc_info = Doctor.enterDrInfo()
        formatted = Doctor.formatDrInfo(doc_info)
        Doctor.addDrToFile(formatted)
        print('\n')

      elif selection_doc == 5:
        request_id = input("Please enter the id of the doctor whose information you want to edit: ")
        doc_info = Doctor.editDoctorInfo(request_id)
        formatted_doc = Doctor.formatDrInfo(doc_info)
        Doctor.writeListOfDoctorsToFile(formatted_doc)
        print('\n')

  elif selection == 2:
    selection_fac = 4
    while not (selection_fac == 3):
      print("""
  Facilities Menu: 
  1 - Display Facilities list
  2 - Add Facility
  3 - Back to the Main Menu""")
      
      selection_fac = int(input("\nSelection: "))

      if selection_fac == 1:
        Facility.displayFacilities()
        print('\n')

      elif selection_fac == 2:
        Facility.addFacility()
        print('\n')
      
      elif selection_fac == 0:
        break

  elif selection == 3:
    selection_lab = 4
    while not (selection_lab == 3):
      print("""
  Laboratories Menu:
  1 - Display laboratories list
  2 - Add laboratory
  3 - Back to the Main Menu""")
      selection_lab = int(input("Selection: "))

      if selection_lab == 1:
        Laboratory.displayLabsList()
      
      if selection_lab == 2:
        Laboratory.addLabToFile()


  elif selection == 4:
    selection_pat = 6
    while not (selection_pat == 5):
      print("""Patients Menu:
  1 - Display patients List
  2 - Search for patient by ID
  3 - Add patient
  4 - Edit patient info
  5 - Back to the Main Menu""")
      selection_pat = int(input("\nSelection: "))
      print('\n')

      if selection_pat == 1:
        pat_data_list = Patient.readPatientsFile()
        Patient.displayPatientsList(pat_data_list)
        print('\n')

      elif selection_pat == 2:
        pat_data_list = Patient.readPatientsFile()          
        Patient.searchPatientByld(pat_data_list)
        print('\n')      

      elif selection_pat == 3:
        pat_info = Patient.enterPatientInfo()
        formatted = Patient.formatPatientInfo(pat_info)
        Patient.addPatientToFile(formatted)
        print('\n')

      elif selection_pat == 4:
        request_id = input("Please enter the id of the patient whose information you want to edit: ")
        pat_info = Patient.editPatientInfo(request_id)
        formatted_pat = Patient.formatPatientInfo(pat_info)
        Patient.writeListOfPatientsToFile(formatted_pat)
        print('\n')
