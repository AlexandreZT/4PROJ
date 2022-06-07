from models.users import Student, Teacher, Staff, Tutor
from routes import users
import pandas as pd
import numpy as np
import requests
import pyrebase
import os
from utils.constants import MODULE_ECTS_LIST
from dotenv import load_dotenv
from datetime import datetime
from faker import Faker


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

fake = Faker()

# datasets to migrate - convert NaN to None
campus_staff = pd.read_csv ("../../Data/Liste_CampusStaff.csv", sep=';').astype(object).replace(np.nan, None)
teachers = pd.read_csv ("../../Data/Liste_Intervenants.csv", sep=',').astype(object).replace(np.nan, None)
student_admin = pd.read_csv ("../../Data/Liste_Etudiant_Administratifs.csv", sep=';', encoding = "ISO-8859-1").astype(object).replace(np.nan, None)
student_alternance = pd.read_csv ("../../Data/Liste_Etudiant_Alternance.csv", sep=';', encoding = "ISO-8859-1").astype(object).replace(np.nan, None)
student_compta = pd.read_csv ("../../Data/Liste_Etudiant_Compta.csv", sep=';', encoding = "ISO-8859-1").astype(object).replace(np.nan, None)
student_pedago = pd.read_csv ("../../Data/Liste_Etudiant_Pédagogie_Notes.csv", sep=';', encoding = "ISO-8859-1").astype(object).replace(np.nan, None)


def staffs_migration():
    i = 0
    for staff in campus_staff.iterrows():
        email=staff[1]['email']
        if users.user_email_already_registred(db, email) == False:
            if i >= 20:
                break
            users.create_staff(
                db=db, 
                auth=auth,
                firstname=staff[1]['first_name'],
                lastname=staff[1]['last_name'],
                email=staff[1]['email'].replace(" ", ""),
                campus=staff[1]['Campus'],
                phone=None,
                role_name=staff[1]['Roles']
            )
            i+=1
    print(i)

def teachers_migration():
    i = 20
    for row in teachers.iterrows():
        email=row[1]['email']
        if users.user_email_already_registred(db, email) == False:
            if i >= 50:
                break
            users.create_teacher(
                db=db, 
                auth=auth,
                firstname=row[1]['first_name'],
                lastname=row[1]['last_name'],
                email=row[1]['email'].replace(" ", ""),
                modules=row[1]['modules'],
                is_available=None,
                section=row[1]['Section']
            )
            i+=1
    print(i)
    

def students_migration():
    i = 0
    for admin in student_admin.iterrows():
        email=admin[1]['email']
        if users.user_email_already_registred(db, email) == False: # je peux ajouter l'user car il existe pas
            if i >= 20:
                break
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
                if key in MODULE_ECTS_LIST.keys():
                    comment = ""
                    if pedago[key] is not None:
                        comment = fake.sentence(nb_words=fake.random_int(min=0, max=15))
                    pedago_notes.update(
                        {
                            key: {
                                "note": pedago[key],
                                "comment" : comment,
                                "ects" : MODULE_ECTS_LIST[key]
                            }
                        }
                    )

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
            i+=1
    print(i)

def tutor_migration():
    
    number_of_generated_tutors = 10
    for _ in range(number_of_generated_tutors): 
        email = fake.company_email()
        if users.user_email_already_registred(db, email) == False:
            firstname= fake.first_name()
            lastname = fake.last_name()
            enterprise_location = fake.address()
            phone = fake.phone_number()
            email = fake.company_email()
            enterprise_name = email.split('@')[1].split('.')[0]
            gender = np.random.choice(["Male", "Female"], p=[0.5, 0.5])
            job = fake.job()
            date_of_birth = str(fake.date_of_birth())
            student_apprentices=[]
            users.create_tutor(
                db=db,
                auth=auth,
                firstname=firstname,
                lastname=lastname,
                email=email,
                phone=phone,
                enterprise_name=enterprise_name,
                enterprise_location=enterprise_location, 
                gender=gender,
                job=job,
                date_of_birth=date_of_birth,
                student_apprentices=student_apprentices
            )
        else:
            number_of_generated_tutors+1 # on veut créer le nombre de tuteur demandé ainsi lorsqu'un email avait déjà été utilisé on recommence.

        # print(fake.word())
        # fake.random_int(0, 100)
        # get email of student he got
        

# ici tu choisi les migrations souhaté
if __name__ == '__main__':
    students_migration()
    staffs_migration()
    teachers_migration()
    tutor_migration()