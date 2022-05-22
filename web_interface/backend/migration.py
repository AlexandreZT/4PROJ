from models.users import Student, Teacher, Staff, Tutor, MODULE_CODE_LIST
from routes import users
import pandas as pd
import requests
import pyrebase
import os
from dotenv import load_dotenv
from datetime import datetime


load_dotenv('.env')

firebaseConfig = {
    'apiKey': os.getenv("apiKey"), 
    'authDomain': os.getenv("authDomain"),
    'databaseURL': os.getenv("databaseURL"),
    'projectId': os.getenv("projectId"),
    'storageBucket': os.getenv("storageBucket"),
    'messagingSenderId': os.getenv("messagingSenderId"),
    'appId': os.getenv("appId"),
    'measurementId': os.getenv("measurementId")
}

firebase=pyrebase.initialize_app(firebaseConfig)

db=firebase.database()

auth=firebase.auth()

storage=firebase.storage()

# datasets to migrate - convert NaN to None
campus_staff = pd.read_csv ("../../Data/Liste_CampusStaff.csv", sep=';').astype(object).replace(pd.np.nan, None)
teachers = pd.read_csv ("../../Data/Liste_Intervenants.csv", sep=',').astype(object).replace(pd.np.nan, None)
student_admin = pd.read_csv ("../../Data/Liste_Etudiant_Administratifs.csv", sep=';', encoding = "ISO-8859-1").astype(object).replace(pd.np.nan, None)
student_alternance = pd.read_csv ("../../Data/Liste_Etudiant_Alternance.csv", sep=';', encoding = "ISO-8859-1").astype(object).replace(pd.np.nan, None)
student_compta = pd.read_csv ("../../Data/Liste_Etudiant_Compta.csv", sep=';', encoding = "ISO-8859-1").astype(object).replace(pd.np.nan, None)
student_pedago = pd.read_csv ("../../Data/Liste_Etudiant_Pédagogie_Notes.csv", sep=';', encoding = "ISO-8859-1").astype(object).replace(pd.np.nan, None)
tutor = pd.read_csv ("../../Data/Liste_Tuteurs.csv", sep=';', encoding = "ISO-8859-1") .astype(object).replace(pd.np.nan, None)

def staffs_migration():
    for row in campus_staff.iterrows():
        users.create_staff(
            db=db, 
            auth=auth,
            first_name=row[1]['first_name'],
            last_name=row[1]['last_name'],
            email=row[1]['email'],
            Campus=row[1]['Campus'],
            Roles=row[1]['Roles']
        )

def teachers_migration():
    for row in teachers.iterrows():
        users.create_teachers(
            db=db, 
            auth=auth,
            firs_tname=row[1]['first_name'],
            last_name=row[1]['last_name'],
            email=row[1]['email'],
            modules=row[1]['modules'],
            Section=row[1]['Section']
        )
    print(teachers)
    

def students_migration():

    for admin in student_admin.iterrows():
        email=admin[1]['email']
        print(email)
        if users.user_email_already_registred(db, email) == False: # je peux ajouter l'user car il existe pas
            alternance = None
            for user in student_alternance.iterrows():
                if user[1]['email'] == email:
                    alternance = user[1]
                    break

            compta = None
            for user in student_compta.iterrows():
                if user[1]['email'] == email:
                    compta = user[1]
                    break
                    

            pedago = None
            for user in student_pedago.iterrows():
                if user[1]['email'] == email:
                    pedago = user[1]
                    break

            pedago_notes = {}
            for key in student_pedago.keys():
                if key in MODULE_CODE_LIST:
                    pedago_notes.update({key: pedago[key]})

            users.create_student(
                db=db, 
                auth=auth,
                # data administrative
                firstname=admin[1]['first_name'],
                lastname=admin[1]['last_name'],
                email=admin[1]['email'].replace(" ", ""),
                campus=admin[1]['campus'],
                date_of_birth=admin[1]['date_of_birth'],
                year_of_birth=admin[1]['year_of_birth'],
                street_address=admin[1]['street_address'],
                gender=admin[1]['gender'],
                region=admin[1]['region'],
                speciality=admin[1]['speciality'],
                previous_level=admin[1]['previous_level'],
                nbre_absence=admin[1]['nbre_absence'],
                age_of_entry=admin[1]['age_of_entry'],
                # data compta
                entry_level=compta['entry_level'],
                year_of_entry=compta['year_of_entry'],
                year_of_exit=compta['year_of_exit'],
                study_lenght=compta['study_lenght'],
                level_of_exit=compta['level_of_exit'],
                still_student=compta['still_student'],
                compta_payment_type=compta['compta_paymentType'],
                compta_paid=compta['compta_paid'],
                compta_payment_due=compta['compta_paymentDue'],
                compta_relance=compta['compta_relance'],
                # data alternance
                level=alternance['level'],
                contratPro=alternance['contratPro'],
                is_hired=alternance['is_hired'],
                lenght_month_hired=alternance['lenght_month_hired'],
                company_hired=alternance['company_hired'],
                entreprise_alternance=alternance['entreprise_alternance'],
                entreprise_alternance_address=alternance['entreprise_alternance_address'],
                poste_occupe=alternance['poste_occupe'],
                secteur_entreprise=alternance['secteur_activite_entreprise_alternance'],
                date_debut_alternance=str(alternance['date_debut_alternance']),
                # data pedago
                pedago=pedago_notes
            )

# ici tu choisi les fonctions que tu veux executer
if __name__ == '__main__':
    students_migration()
    # staffs_migration()
    # teachers_migration()
    # students_migration()