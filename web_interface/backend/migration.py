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

df = pd.read_csv ("../../Data/Liste_CampusStaff.csv", sep=';')  # defualt value is ','

for row in df.iterrows():
    
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

    



