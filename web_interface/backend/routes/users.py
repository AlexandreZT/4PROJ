from pyasn1.type.univ import Null

from models.users import User, Student


def create_user(db, auth, firstname, lastname, email):
    """
    Used for create manually a user from the web interface, email is unique
    TODO : return email already used if it is.
    """
    
    # set my own id (from firestore auth):
    auth_data = auth.create_user_with_email_and_password(email, password="password")
    print("auth_data: ", auth_data)
    

    db.child("users").child(auth_data["localId"]).set(
        User(
            # mandatory used for creation, if you got more data you can add more details
            firstname=firstname.title(),
            lastname=lastname.upper(),
            email=email.lower()
        )
    )

    # db.child("users").child(auth_data["localId"]).set({
    #     "firstname" : firstname.title(),
    #     "lastname" : lastname.upper(),
    #     "email" : email.lower(),
    #     "phone" : phone,
    #     "type" : type,
    #     "uid" : auth_data["localId"] # temporarily
    # })

# TODO AND IN PROGRESS
def create_student(db, auth, firstname, lastname, email):
    """
    Used for create manually a user from the web interface, email is unique
    TODO : return email already used if it is.
    """
    
    # set my own id (from firestore auth):
    auth_data = auth.create_user_with_email_and_password(email, password="password")
    print("auth_data: ", auth_data)
    
    db.child("users").child(auth_data["localId"]).set(
        Student(
            # mandatory used for creation, if you got more data you can add more details
            firstname=firstname.title(),
            lastname=lastname.upper(),
            email=email.lower(),
            # details optionals, if not filled other method will permit you to edit later
            campus="Paris",
            date_of_birth="02/10/1979",
            year_of_birth="1979",
            street_address="40 Nova Crossing",
            gender="male",
            region="str",
            level="M.ENG 1",
            speciality="Intelligence Artificielle",
            contratPro=True,
            previous_level="Bac",
            nbre_absence=4,
            age_of_entry=22
            # ...
        ).__dict__
        # les champs du model à None ne seront pas enregistré en base
    )

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
    types = ["students", "teachers", "staffs", "tutors"]

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
    
def get_all_students_data(db):
    users = db.child("users").get()
    data={}

    for user in users.each():
        if user.val()['type'] == "students":
            data.update({user.key() : user.val()})

    return data

def get_all_teachers_data(db):
    users = db.child("users").get()
    data={}

    for user in users.each():
        if user.val()['type'] == "teachers":
            data.update({user.key() : user.val()})

    return data

def get_all_staffs_data(db):
    users = db.child("users").get()
    data={}

    for user in users.each():
        if user.val()['type'] == "staffs":
            data.update({user.key() : user.val()})

    return data

def get_all_tutors_data(db):
    users = db.child("users").get()
    data={}

    for user in users.each():
        if user.val()['type'] == "tutors":
            data.update({user.key() : user.val()})

    return data


def delete_user_with_id(db, id, auth):
    # TODO delete user in Authentication service bcoz there is no duplication
    # user = auth.sign_in_with_email_and_password(email, password)
    # auth.delete_user_account(user['idToken']) # must be signed in 
    db.child("users").child(id).remove()


# + : .order_by_child(string), .start_at(int), .end_at(int)