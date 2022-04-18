from pyasn1.type.univ import Null

from models.users import User, Student, Staff, Teacher


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
def create_student(db, auth, firstname, lastname, email, campus, date_of_birth, year_of_birth, street_address, gender,
        region, level, speciality, contratPro, previous_level, nbre_absence, age_of_entry, is_hired, lenght_month_hired,
        company_hired, entreprise_alternance, entreprise_alternance_address, poste_occupe, secteur_entreprise,
        date_debut_alternance, entry_level, year_of_entry, year_of_exit, study_lenght, level_of_exit, still_student,	
        compta_payment_type, compta_paid, compta_payment_due, compta_relance):
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
            campus=campus.lower(),
            date_of_birth=date_of_birth.lower(),
            year_of_birth=year_of_birth,
            street_address=street_address.lower(),
            gender=gender.lower(),
            region=region.lower(),
            level=level.lower(),
            speciality=speciality.lower(),
            contratPro=contratPro,
            previous_level=previous_level.lower(),
            nbre_absence=nbre_absence,
            age_of_entry=age_of_entry,
            is_hired=is_hired,
            lenght_month_hired=lenght_month_hired,
            company_hired=company_hired.lower(),
            entreprise_alternance=entreprise_alternance.lower(),
            entreprise_alternance_address=entreprise_alternance_address.lower(),
            poste_occupe=poste_occupe.lower(),
            secteur_entreprise=secteur_entreprise.lower(),
            date_debut_alternance=date_debut_alternance.lower(),
            entry_level=entry_level.lower(),
            year_of_entry=year_of_entry,
            year_of_exit=year_of_exit,
            study_lenght=study_lenght,
            level_of_exit=level_of_exit.lower(),
            still_student=still_student,
            compta_payment_type=compta_payment_type.lower(),
            compta_paid=compta_paid,
            compta_payment_due=compta_payment_due,	
            compta_relance=compta_relance,
        ).__dict__
        # les champs du model à None ne seront pas enregistré en base
    )

def create_staff(db, auth, firstname, lastname, email):
    """
    Used for create manually a user from the web interface, email is unique
    TODO : return email already used if it is.
    """
    
    # set my own id (from firestore auth):
    auth_data = auth.create_user_with_email_and_password(email, password="password")
    print("auth_data: ", auth_data)
    
    
    db.child("users").child(auth_data["localId"]).set(
        Staff(
            # mandatory used for creation, if you got more data you can add more details
            firstname=firstname.title(),
            lastname=lastname.upper(),
            email=email.lower(),
            # details optionals, if not filled other method will permit you to edit later

        ).__dict__
        # les champs du model à None ne seront pas enregistré en base
    )

def create_teacher(db, auth, firstname, lastname, email):
    """
    Used for create manually a user from the web interface, email is unique
    TODO : return email already used if it is.
    """
    
    # set my own id (from firestore auth):
    auth_data = auth.create_user_with_email_and_password(email, password="password")
    print("auth_data: ", auth_data)

    db.child("users").child(auth_data["localId"]).set(
        Teacher(
            # mandatory used for creation, if you got more data you can add more details
            firstname=firstname.title(),
            lastname=lastname.upper(),
            email=email.lower(),
            # details optionals, if not filled other method will permit you to edit later
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