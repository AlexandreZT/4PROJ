import pyrebase
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

# -------------- GET DATA

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

# -------------- CREATE USERS

@app.route('/create-student', methods=['POST'])
def create_student():
    if request.method != 'POST': 
        return Response(status=404)
    
    firstname = request.json["firstname"]
    lastname = request.json["lastname"]
    email = request.json["email"]
    campus = request.json["campus"]
    date_of_birth = request.json["date_of_birth"]
    year_of_birth = request.json["year_of_birth"]
    street_address = request.json["street_address"]
    gender = request.json["gender"]
    region = request.json["region"]
    level = request.json["level"]
    speciality = request.json["speciality"]
    contratPro = request.json["contratPro"]
    previous_level = request.json["previous_level"]
    nbre_absence = request.json["nbre_absence"]
    age_of_entry = request.json["age_of_entry"]
    is_hired = request.json["is_hired"]
    lenght_month_hired = request.json["lenght_month_hired"]
    company_hired = request.json["company_hired"]
    entreprise_alternance = request.json["entreprise_alternance"]
    entreprise_alternance_address = request.json["entreprise_alternance_address"]
    poste_occupe = request.json["poste_occupe"]
    secteur_entreprise = request.json["secteur_entreprise"]
    date_debut_alternance = request.json["date_debut_alternance"]
    entry_level = request.json["entry_level"]
    year_of_entry = request.json["year_of_entry"]
    year_of_exit = request.json["year_of_exit"]
    study_lenght = request.json["study_lenght"]
    level_of_exit = request.json["level_of_exit"]
    still_student = request.json["still_student"]
    compta_payment_type = request.json["compta_payment_type"]
    compta_paid = request.json["compta_paid"]
    compta_payment_due = request.json["compta_payment_due"]
    compta_relance = request.json["compta_relance"]

    users.create_student(db, auth, firstname, lastname, email, campus, date_of_birth, year_of_birth, street_address, gender,
        region, level, speciality, contratPro, previous_level, nbre_absence, age_of_entry, is_hired, lenght_month_hired,
        company_hired, entreprise_alternance, entreprise_alternance_address, poste_occupe, secteur_entreprise,
        date_debut_alternance, entry_level, year_of_entry, year_of_exit, study_lenght, level_of_exit, still_student,	
        compta_payment_type, compta_paid, compta_payment_due, compta_relance)
    
    return Response(status=200)

@app.route('/create-staff', methods=['POST'])
def create_staff():
    if request.method != 'POST': 
        return Response(status=404)
    
    firstname = request.json["firstname"]
    lastname = request.json["lastname"]
    email = request.json["email"]
    campus = request.json["campus"]
    phone = request.json ["phone"]
    role_name = request.json["role_name"]

    users.create_staff(db, auth, firstname, lastname, email, campus, phone, role_name)
    
    return Response(status=200)

@app.route('/create-teacher', methods=['POST'])
def create_teacher():
    if request.method != 'POST': 
        return Response(status=404)
    
    firstname = request.json["firstname"]
    lastname = request.json["lastname"]
    email = request.json["email"]
    campus = request.json["campus"]
    modules = request.json["modules"]
    is_available = request.json["is_available"]
    
    users.create_teacher(db, auth, firstname, lastname, email, campus, modules, is_available)
    
    return Response(status=200)

@app.route('/create-tutor', methods=['POST'])
def create_tutor():
    if request.method != 'POST': 
        return Response(status=404)
    
    firstname = request.json["firstname"]
    lastname = request.json["lastname"]
    email = request.json["email"]
    phone = request.json["phone"]
    enterprise_name = request.json["enterprise_name"]
    enterprise_location = request.json["enterprise_location"]
    
    users.create_tutor(db, auth, firstname, lastname, email, phone, enterprise_name, enterprise_location)
    
    return Response(status=200)

# -------------- DELETE DATA

@app.route('/delete-user-with-id', methods=['DELETE'])
def delete_user_with_id():
    if request.method != 'DELETE': 
        return Response(status=404)

    id = request.json["id"]

    users.delete_user_with_id(db, id, auth)

    return Response(status=200)

# -------------- UPDATE DATA

@app.route('/update-student-data-by-id', methods=['PUT'])
def update_student_data_by_id():
    if request.method != 'PUT': 
        return Response(status=404)

    id = request.json["id"]
    firstname = request.json["firstname"]
    lastname = request.json["lastname"]
    email = request.json["email"]

    response = users.update_student_data_by_id(db, id, firstname, lastname, email)
    if response == 404:
        return Response(status=404)
    return Response(status=200)

@app.route('/update-staff-data-by-id', methods=['PUT'])
def update_staff_data_by_id():
    if request.method != 'PUT': 
        return Response(status=404)

    id = request.json["id"]
    firstname = request.json["firstname"]
    lastname = request.json["lastname"]
    email = request.json["email"]

    response = users.update_staff_data_by_id(db, id, firstname, lastname, email)
    if response == 404:
        return Response(status=404)
    return Response(status=200)

@app.route('/update-tutor-data-by-id', methods=['PUT'])
def update_tutor_data_by_id():
    if request.method != 'PUT': 
        return Response(status=404)

    id = request.json["id"]
    firstname = request.json["firstname"]
    lastname = request.json["lastname"]
    email = request.json["email"]

    response = users.update_tutor_data_by_id(db, id, firstname, lastname, email)
    if response == 404:
        return Response(status=404)
    return Response(status=200)

@app.route('/update-teacher-data-by-id', methods=['PUT'])
def update_teacher_data_by_id():
    if request.method != 'PUT': 
        return Response(status=404)

    id = request.json["id"]
    firstname = request.json["firstname"]
    lastname = request.json["lastname"]
    email = request.json["email"]

    response = users.update_teacher_data_by_id(db, id, firstname, lastname, email)
    if response == 404:
        return Response(status=404)
    return Response(status=200)

# -------------- UTILITY

@app.route('/sign-in', methods=['POST'])
def sign_in():
    if request.method != 'POST': 
        return Response(status=404)

    email = request.json["email"]
    password = request.json["password"]
    
    code = users.sign_in(auth, email, password)
    return Response(status=code)

@app.route('/forgotten-password', methods=['POST'])
def forgotten_password():
    if request.method != 'POST': 
        return Response(status=404)
    try:
        resp = auth.send_password_reset_email(request.json["email"])
    except:
        return Response(response="Le mail n'existe pas", status=403)

    return Response(response="Un mail a été envoyé pour reset votre mot de passe.", status=200)
    
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
    app.run(debug=True, host='0.0.0.0', port=5000) # ssl_context=("./cert.pem", "./key.pem")

# # NOTES # #
# More firebase auth features :
## auth.send_email_verification(login['idToken'])
## auth.send_password_reset_email(email)
