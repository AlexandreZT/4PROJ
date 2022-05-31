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
    return Response(response="(╯‵□′)╯︵┻━┻", status=200)

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

@app.route('/student/<id>/pedago', methods=['GET'])
def get_student_pedago_by_email_or_id(id):
    if request.method != 'GET': 
        return Response(status=404)

    response, status = users.get_student_pedago_by_email_or_id(db, id)

    return jsonify(response), status

@app.route('/student/<id>/comptability', methods=['GET'])
def get_student_comptability_by_email_or_id(id):
    if request.method != 'GET': 
        return Response(status=404)

    response, status = users.get_student_comptabilty_by_email_or_id(db, id)

    return jsonify(response), status

@app.route('/student/<id>/contract', methods=['GET'])
def get_student_contract_by_email_or_id(id):
    if request.method != 'GET': 
        return Response(status=404)

    response, status = users.get_student_contract_by_email_or_id(db, id)

    return jsonify(response), status

@app.route('/student/<id>/absences', methods=['GET'])
def get_student_absences_by_email_or_id(id):
    if request.method != 'GET': 
        return Response(status=404)

    response, status = users.get_student_absences_by_email_or_id(db, id)

    return jsonify(response), status
       

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
    year_of_birth = date_of_birth.split("-")[0]
    street_address = request.json["street_address"]
    gender = request.json["gender"]
    region = request.json["region"]
    level = request.json["level"]
    speciality = request.json["speciality"]
    contratPro = request.json["contratPro"]
    previous_level = request.json["previous_level"]
    nbre_absence = None
    age_of_entry = request.json["age_of_entry"]
    # not in form
    is_hired = None
    lenght_month_hired = None
    company_hired = None
    entreprise_alternance = None
    entreprise_alternance_address = None
    poste_occupe = None
    secteur_entreprise = None
    date_debut_alternance = None
    entry_level = None
    year_of_entry = None
    year_of_exit = None
    study_lenght = None
    level_of_exit = None
    still_student = None
    compta_payment_type = None
    compta_paid = None
    compta_payment_due = None
    compta_relance = None
    pedago = {}

    users.create_student(db, auth, firstname, lastname, email, campus, date_of_birth, year_of_birth, street_address, gender,
        region, level, speciality, contratPro, previous_level, nbre_absence, age_of_entry, is_hired, lenght_month_hired,
        company_hired, entreprise_alternance, entreprise_alternance_address, poste_occupe, secteur_entreprise,
        date_debut_alternance, entry_level, year_of_entry, year_of_exit, study_lenght, level_of_exit, still_student,	
        compta_payment_type, compta_paid, compta_payment_due, compta_relance, pedago)
    
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
    section = request.json["section"]
    modules = None # request.json["modules"]
    is_available = None # request.json["is_available"]
    
    users.create_teacher(db, auth, firstname, lastname, email, section, modules, is_available)
    
    return Response(status=200)

@app.route('/create-tutor', methods=['POST'])
def create_tutor():
    if request.method != 'POST': 
        return Response(status=404)
    
    firstname = request.json["firstname"]
    lastname = request.json["lastname"]
    email = request.json["email"]
    phone = request.json["phone"]
    gender = request.json["gender"]
    enterprise_name = request.json["enterprise_name"]
    enterprise_location = request.json["enterprise_location"]
    job  = request.json["job"]
    date_of_birth = None
    student_apprentices = []

    users.create_tutor(db, auth, firstname, lastname, email, phone, gender, enterprise_name, enterprise_location, job, date_of_birth, student_apprentices)
    
    return Response(status=200)

# -------------- DELETE DATA

@app.route('/delete-only-user-data-with-id', methods=['DELETE'])
def delete_only_user_data_with_id():
    if request.method != 'DELETE': 
        return Response(status=404)

    id = request.json["id"]

    users.delete_only_user_data_with_id(db, id)

    return Response(status=200)

@app.route('/delete-user-with-credentials', methods=['DELETE'])
def delete_user_with_id():
    if request.method != 'DELETE': 
        return Response(status=404)

    email = request.json["email"]
    password = request.json["password"]

    users.delete_user_with_credentials(db, auth, email, password)

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

@app.route('/student/update/pedago', methods=['PUT'])
def update_student_pedago_by_email_or_id():
    if request.method != 'PUT': 
        return Response(status=404)

    id = request.json["id"]
    pedago = request.json["pedago"]

    response = users.update_student_pedago_by_email_or_id(db, id, pedago)
    
    if response == 404:
        return Response(status=404)
    return Response(status=200)

@app.route('/student/update/comptability', methods=['PUT'])
def update_student_comptability_by_email_or_id():
    if request.method != 'PUT': 
        return Response(status=404)

    id = request.json["id"]
    compta = request.json["compta"]

    response = users.update_student_comptability_by_email_or_id(db, id, compta)
    
    if response == 404:
        return Response(status=404)
    return Response(status=200)

@app.route('/student/update/contract', methods=['PUT'])
def update_student_contract_by_email_or_id():
    if request.method != 'PUT': 
        return Response(status=404)

    id = request.json["id"]
    contract = request.json["contratPro"]

    response = users.update_student_contract_by_email_or_id(db, id, contract)
    
    if response == 404:
        return Response(status=404)
    return Response(status=200)

@app.route('/student/update/info', methods=['PUT'])
def update_student_info_by_email_or_id():
    if request.method != 'PUT': 
        return Response(status=404)

    id = request.json["id"]
    email = request.json["email"]
    firstname = request.json["firstname"]
    lastname = request.json["lastname"]
    user_type = request.json["user_type"]

    response = users.update_student_info_by_email_or_id(db, id, email, firstname, lastname, user_type)
    
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
    Return the full db
    """
    if request.method != 'GET': 
        return Response(status=404)

    full_data = db.get().val()

    return jsonify(full_data) 

    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) # ssl_context=("./cert.pem", "./key.pem")

# # NOTES # #
# More firebase auth features :
## auth.send_email_verification(login['idToken'])
