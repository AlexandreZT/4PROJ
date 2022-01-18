from pyasn1.type.univ import Null


def create_user(db, auth, firstname, lastname, email, phone, password, type):
    """
    Used for create manually a user from the web interface, email is unique
    TODO : return email already used if it is.
    """
    
    # set my own id (from firestore auth):
    auth_data = auth.create_user_with_email_and_password(email, password)
    print("auth_data: ", auth_data)

    db.child("users").child(auth_data["localId"]).set({
        "firstname" : firstname.title(),
        "lastname" : lastname.upper(),
        "email" : email.lower(),
        "phone" : phone,
        "type" : type,
        "uid" : auth_data["localId"] # temporarily
    })

def sign_in(auth, email, password):
    """
    Seach in db email == email and password == password
    It would be not enouth, I have to set unique email in db
    """
    try:        
        auth_data = auth.sign_in_with_email_and_password(email, password)
        print(auth_data)
    except Exception as e:
        print("mot de passe incorrect")
        return 404
    else:
        return auth_data

def get_firstname_from_id(db, id):
    return db.child("users").child(id).get().val()['firstname']

def get_all_users_data(db):
    return db.child("users").get().val()

def get_user_data_with_id(db, id):
    return db.child("users").child(id).get().val()

def update_user_data_with_id(db, id, firstname, lastname, email, phone, type):    
    types = ["owner", "customer", "cook", "waiter", "barman"]

    try:
        data = db.child("users").child(id).get().val()
    
        if firstname == "":
            firstname = data['firstname']

        if lastname == "":
            lastname = data['lastname']

        if email == "":
            email = data['email']

        if phone == "":
            phone = data['phone']

        if type == "":
            type = data['type']

        if type in types:
            db.child("users").child(id).update(
                {
                    "firstname" : firstname.title(),
                    "lastname" : lastname.upper(),
                    "email" : email.lower(),
                    "phone" : phone,
                    "type" : type
                }
            )
        else:
            print("ce role n'existe pas")
    except:
        return 404
    
def get_all_cooks_data(db):
    users = db.child("users").get()
    data={}

    for user in users.each():
        if user.val()['type'] == "cook":
            data.update({user.key() : user.val()})

    return data

def get_all_waiters_data(db):
    users = db.child("users").get()
    data={}

    for user in users.each():
        if user.val()['type'] == "waiter":
            data.update({user.key() : user.val()})

    return data

def get_all_customers_data(db):
    users = db.child("users").get()
    data={}

    for user in users.each():
        if user.val()['type'] == "customer":
            data.update({user.key() : user.val()})

    return data

def get_all_owners_data(db):
    users = db.child("users").get()
    data={}

    for user in users.each():
        if user.val()['type'] == "owner":
            data.update({user.key() : user.val()})

    return data

def get_all_barmen_data(db):
    users = db.child("users").get()
    data={}

    for user in users.each():
        if user.val()['type'] == "barman":
            data.update({user.key() : user.val()})

    return data    

def delete_user_with_id(db, id, auth):
    # user = auth.sign_in_with_email_and_password(email, password)
    # auth.delete_user_account(user['idToken']) # must be signed in 
    db.child("users").child(id).remove()


# + : .order_by_child(string), .start_at(int), .end_at(int)