import pyrebase # pip install pyrebase4
import os
from dotenv import load_dotenv
from routes import users
from flask import Flask, jsonify, request, abort, Response
from flask_cors import CORS, cross_origin
import json
from datetime import datetime   

app = Flask(__name__)

CORS(app)

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

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

@app.route('/', methods=['GET'])
def home():
    if request.method != 'GET': 
        return Response(status=404)
    return Response(status=200)

@app.route('/users', methods=['GET'])
def get_all_users_data():
    if request.method != 'GET': 
        return Response(status=404)    
    return jsonify(users.get_all_users_data(db))

@app.route('/user/<id>', methods=['GET'])
def get_user_data_with_id(id):
    if request.method != 'GET': 
        return Response(status=404)
    return jsonify(users.get_user_data_with_id(db, id))

@app.route('/staffs', methods=['GET'])
def get_all_staffs_data():
    if request.method != 'GET': 
        return Response(status=404)
    return jsonify(users.get_all_staffs_data(db))

@app.route('/tutors', methods=['GET'])
def get_all_tutors_data():
    if request.method != 'GET': 
        return Response(status=404)
    return jsonify(users.get_all_tutors_data(db))    

@app.route('/teachers', methods=['GET'])
def get_all_teachers_data():
    if request.method != 'GET': 
        return Response(status=404)
    return jsonify(users.get_all_teachers_data(db))

@app.route('/students', methods=['GET'])
def get_all_students_data():
    if request.method != 'GET': 
        return Response(status=404)
    return jsonify(users.get_all_students_data(db))    

#------------------------------------------

@app.route('/create-user', methods=['POST'])
def create_user():
    if request.method != 'POST': 
        return Response(status=404)

    firstname = request.json["firstname"]
    lastname = request.json["lastname"]
    email = request.json["email"]
    phone = request.json["phone"]
    password = request.json["password"]
    type = request.json["type"]

    users.create_user(db, auth, firstname, lastname, email, phone, password, type)    

    return Response(status=200)

@app.route('/sign-in', methods=['POST'])
def sign_in():
    if request.method != 'POST': 
        return Response(status=404)

    email = request.json["email"]
    password = request.json["password"]
    
    users.sign_in(auth, email, password)

    return Response(status=200)

@app.route('/delete-user-with-id', methods=['DELETE'])
def delete_user_with_id():
    if request.method != 'DELETE': 
        return Response(status=404)

    id = request.json["id"]

    users.delete_user_with_id(db, id, auth)

    return Response(status=200)

@app.route('/update-user-data-with-id', methods=['PUT'])
def update_user_data_with_id():
    if request.method != 'PUT': 
        return Response(status=404)

    id = request.json["id"]
    firstname = request.json["firstname"]
    lastname = request.json["lastname"]
    email = request.json["email"]
    phone = request.json["phone"]
    type = request.json["type"]

    response = users.update_user_data_with_id(db, id, firstname, lastname, email, phone, type)
    if response == 404:
        return Response(status=404)
    return Response(status=200)

@app.route('/data', methods=['GET'])
def get_all_data():
    """
    We store backup on firebase and keep the last on server / downloadable
    """
    if request.method != 'GET': 
        return Response(status=404)

    date = datetime.now()

    date = date.strftime("%d-%m-%Y_%Hh%M")
    full_data = db.get().val()
    with open('backup.json', 'w') as json_file:
        json.dump(full_data, json_file)

    storage.child('backup_'+date+'.json').put('backup.json')
    return jsonify(full_data) 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

# # NOTES # #
# More firebase auth features :
## auth.send_email_verification(login['idToken'])
## auth.send_password_reset_email(email)

test