import pyrebase
import os
from dotenv import load_dotenv
import json
from datetime import datetime   

load_dotenv('../env')

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


def create_backup():
    """
    Create a full db backup available on firestore server (storage)
    """
    date = datetime.now()

    date = date.strftime("%d-%m-%Y_%Hh%M")
    full_data = db.get().val()

    with open('backup.json', 'w') as json_file:
        json.dump(full_data, json_file)

    storage.child('backup_'+date+'.json').put('backup.json')

if __name__ == '__main__':
    create_backup()