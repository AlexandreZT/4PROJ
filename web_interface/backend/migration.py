from models.users import Student, Teacher, Staff, Tutor
from routes import users
import pandas as pd
import requests
import pyrebase
import os
from dotenv import load_dotenv
import json
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

# datasets to migrate
campus_staff = pd.read_csv ("../../Data/Liste_CampusStaff.csv", sep=';')
teachers = pd.read_csv ("../../Data/Liste_Intervenants.csv", sep=',')
student_admin = pd.read_csv ("../../Data/Liste_Etudiant_Administratifs.csv", sep=';', encoding = "ISO-8859-1")
student_alternance = pd.read_csv ("../../Data/Liste_Etudiant_Alternance.csv", sep=';', encoding = "ISO-8859-1")
student_compta = pd.read_csv ("../../Data/Liste_Etudiant_Compta.csv", sep=';', encoding = "ISO-8859-1")
student_pedago = pd.read_csv ("../../Data/Liste_Etudiant_Pédagogie_Notes.csv", sep=';', encoding = "ISO-8859-1")

def staffs_migration():
    for row in campus_staff.iterrows():
        users.create_staff(
            db=db, 
            auth=auth,
            firstname=row[1]['first_name'],
            lastname=row[1]['last_name'],
            email=row[1]['email'],
            campus=row[1]['Campus'],
            role_name=row[1]['Roles'],
            phone=''
        )

def teachers_migration():
    print(teachers)

def students_migration():
    print(student_admin)
    print(student_alternance)
    print(student_compta)
    print(student_pedago)


# ici tu choisi les fonctions que tu veux executer
if __name__ == '__main__':
    # staffs_migration()
    teachers_migration()
    # students_migration()