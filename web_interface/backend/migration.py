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

df = pd.read_csv (r'../../Data/Liste_CampusStaff.csv')
# for index,row in df.iterrows() :
#     print (df[row])
for index in df.itertuples():
    # print(index[1].split(';')[1])

    users.create_staff(db=db, auth=auth,
        firstname=index[1].split(';')[1],
        lastname=index[1].split(';')[2],
        email=index[1].split(';')[3],
        campus=index[1].split(';')[4],
        role_name=index[1].split(';')[5],
        phone='')

    



