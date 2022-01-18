import pyrebase # pip install pyrebase4
import os
from dotenv import load_dotenv
from routes import users, menu, tables, booking, stocks, sells
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

@app.route('/menu', methods=['GET'])
def get_menu_data():
    if request.method != 'GET': 
        return Response(status=404)
    return jsonify(menu.get_menu_data(db))

@app.route('/user/<id>', methods=['GET'])
def get_user_data_with_id(id):
    if request.method != 'GET': 
        return Response(status=404)
    return jsonify(users.get_user_data_with_id(db, id))

@app.route('/menu/<id>', methods=['GET'])
def get_menu_item_data_with_id(id):
    if request.method != 'GET': 
        return Response(status=404)
    return jsonify(menu.get_menu_item_data_with_id(db, id))

@app.route('/owners', methods=['GET'])
def get_all_owners_data():
    if request.method != 'GET': 
        return Response(status=404)
    return jsonify(users.get_all_owners_data(db))

@app.route('/customers', methods=['GET'])
def get_all_customers_data():
    if request.method != 'GET': 
        return Response(status=404)
    return jsonify(users.get_all_customers_data(db))    

@app.route('/waiters', methods=['GET'])
def get_all_waiters_data():
    if request.method != 'GET': 
        return Response(status=404)
    return jsonify(users.get_all_waiters_data(db))

@app.route('/cooks', methods=['GET'])
def get_all_cooks_data():
    if request.method != 'GET': 
        return Response(status=404)
    return jsonify(users.get_all_cooks_data(db))    

@app.route('/barmen', methods=['GET'])
def get_all_barmen_data():
    if request.method != 'GET': 
        return Response(status=404)
    return jsonify(users.get_all_barmen_data(db))   

@app.route('/foods', methods=['GET'])
def get_all_foods_data():
    if request.method != 'GET': 
        return Response(status=404)
    return jsonify(menu.get_all_foods_data(db)) 

@app.route('/drinks', methods=['GET'])
def get_all_drinks_data():
    if request.method != 'GET': 
        return Response(status=404)
    return jsonify(menu.get_all_drinks_data(db)) 

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

@app.route('/create-product', methods=['POST'])
def create_menu_item():
    if request.method != 'POST': 
        return Response(status=404)

    name = request.json["name"]
    description = request.json["description"]
    price = request.json["price"]
    type = request.json["type"]

    return jsonify(menu.create_menu_item(db, name, description, price, type))
 
@app.route('/delete-user-with-id', methods=['DELETE'])
def delete_user_with_id():
    if request.method != 'DELETE': 
        return Response(status=404)

    id = request.json["id"]

    users.delete_user_with_id(db, id, auth)

    return Response(status=200)

@app.route('/delete-product-with-id', methods=['DELETE'])
def delete_menu_item_with_id():
    if request.method != 'DELETE': 
        return Response(status=404)

    id = request.json["id"]

    menu.delete_menu_item_with_id(db, id)

    return Response(status=200)

@app.route('/update-product-data-with-id', methods=['PUT'])
def update_menu_item_data_with_id():
    if request.method != 'PUT': 
        return Response(status=404)

    id = request.json["id"]
    name = request.json["name"]
    description = request.json["description"]
    price = request.json["price"]
    type = request.json["type"]

    response = menu.update_menu_item_data_with_id(db, id, name, description, price, type)
    if response == 404:
        return Response(status=404)
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

@app.route('/tables', methods=['GET'])
def get_tables():
    if request.method != 'GET': 
        return Response(status=404)

    return jsonify(tables.get_tables(db))

@app.route('/save-booking', methods=['POST'])
def save_booking():
    if request.method != 'POST': 
        return Response(status=404)

    id_user = request.json["idUser"]
    nb_persons = request.json["nbPersons"]
    arrival_time = request.json["arrivalTime"]
    return jsonify(booking.save_booking(db=db, nb_persons=nb_persons, id_user=id_user, arrival_time=arrival_time))

@app.route('/update-object-quantity', methods=['PUT'])
def update_quantity_by_product_name():
    if request.method != 'PUT': 
        return Response(status=404)
 
    status = stocks.update_quantity_by_product_name(db=db, name=request.json["name"], quantity=request.json["quantity"])
    return Response(status=status)

@app.route('/update-table-capacity-by-id', methods=["PUT"])
def update_table_capacity_by_id():
    if request.method != 'PUT':
        return Response(status=404)
        
    id = request.json["id"]
    capacity = request.json["capacity"]

    status = tables.update_table_capacity_by_id(db, id, capacity)
    return Response(status=status)

@app.route('/stocks', methods=["GET"])
def get_stocks():
    if request.method != 'GET':
        return Response(status=404)

    return jsonify(stocks.get_stocks(db))

@app.route('/consumme-product', methods=["PUT"])
def consumme_product():
    if request.method != 'PUT':
        return Response(status=404)

    name = request.json["name"]
    quantity = request.json["quantity"]

    return jsonify(stocks.consumme_product(db=db, name=name, quantity=quantity))

@app.route('/get-services-stats', methods=["GET"]) # TODO
def get_services_stats():
    if request.method != 'GET':
        return Response(status=404)

    return jsonify(sells.get_services_stats(db))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

# # NOTES # #
# More firebase auth features :
## auth.send_email_verification(login['idToken'])
## auth.send_password_reset_email(email)