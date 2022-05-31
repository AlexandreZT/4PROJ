from models.users import User, Student, Staff, Teacher, Tutor


def create_student(db, auth, firstname, lastname, email, campus, date_of_birth, year_of_birth, street_address, gender,
        region, level, speciality, contratPro, previous_level, nbre_absence, age_of_entry, is_hired, lenght_month_hired,
        company_hired, entreprise_alternance, entreprise_alternance_address, poste_occupe, secteur_entreprise,
        date_debut_alternance, entry_level, year_of_entry, year_of_exit, study_lenght, level_of_exit, still_student,	
        compta_payment_type, compta_paid, compta_payment_due, compta_relance, pedago):
    """
    Used for create manually a user from the web interface, email is unique
    TODO : return email already used if it is.
    """
    # set my own id (from firestore auth):
    auth_data = auth.create_user_with_email_and_password(email, password=db.generate_key())
    # print("auth_data: ", auth_data)
    
    # les champs du model à None ne seront pas enregistré en base
    student = Student(
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
        level=level,
        speciality=speciality,
        contratPro=contratPro,
        previous_level=previous_level.lower(),
        nbre_absence=nbre_absence,
        age_of_entry=age_of_entry,
        is_hired=is_hired,
        lenght_month_hired=lenght_month_hired,
        company_hired=company_hired,
        entreprise_alternance=entreprise_alternance,
        entreprise_alternance_address=entreprise_alternance_address,
        poste_occupe=poste_occupe,
        secteur_entreprise=secteur_entreprise,
        date_debut_alternance=date_debut_alternance,
        entry_level=entry_level,
        year_of_entry=year_of_entry,
        year_of_exit=year_of_exit,
        study_lenght=study_lenght,
        level_of_exit=level_of_exit,
        still_student=still_student,
        compta_payment_type=compta_payment_type,
        compta_paid=compta_paid,
        compta_payment_due=compta_payment_due,	
        compta_relance=compta_relance,
        pedago=pedago
    ).__dict__
    
            
    db.child("users").child(auth_data["localId"]).set(student)
    

def create_staff(db, auth, firstname, lastname, email, campus, phone, role_name):
    """
    Used for create manually a user from the web interface, email is unique
    TODO : return email already used if it is.
    """
    # set my own id (from firestore auth):
    auth_data = auth.create_user_with_email_and_password(email, password=db.generate_key())
    # print("auth_data: ", auth_data)
    
    staff = Staff(
            # mandatory used for creation, if you got more data you can add more details
            firstname=firstname.title(),
            lastname=lastname.upper(),
            email=email.lower(),
            campus=campus.upper(), 
            phone=phone,
            role_name=role_name.title()
            # details optionals, if not filled other method will permit you to edit later
        ).__dict__
        # les champs du model à None ne seront pas enregistré en base

    db.child("users").child(auth_data["localId"]).set(staff)


def create_teacher(db, auth, firstname, lastname, email, modules, is_available, section):
    """         
    Used for create manually a user from the web interface, email is unique
    TODO : return email already used if it is.
    """
    # set my own id (from firestore auth):
    auth_data = auth.create_user_with_email_and_password(email, password=db.generate_key())
    # print("auth_data: ", auth_data)

    teacher = Teacher(
        firstname=firstname,
        lastname=lastname,
        email=email,
        modules=modules,
        is_available=is_available,
        section=section,
    ).__dict__

    db.child("users").child(auth_data["localId"]).set(teacher)


def create_tutor(db, auth, firstname, lastname, email, phone, enterprise_name, enterprise_location, gender, job, date_of_birth, student_apprentices):
    """
    Used for create manually a user from the web interface, email is unique
    TODO : return email already used if it is.
    """
    
    # set my own id (from firestore auth):
    auth_data = auth.create_user_with_email_and_password(email, password=db.generate_key())
    # print("auth_data: ", auth_data)
    
    # les champs du model à None ne seront pas enregistré en base
    tutor = Tutor(
            # mandatory used for creation, if you got more data you can add more details
            firstname=firstname.title(),
            lastname=lastname.upper(),
            email=email.lower(),
            phone=phone,
            enterprise_name=enterprise_name.title(),
            enterprise_location=enterprise_location.upper(),
            gender=gender,
            job=job,
            date_of_birth=date_of_birth,
            student_apprentices=student_apprentices
            # details optionals, if not filled other method will permit you to edit later

        ).__dict__
        

    db.child("users").child(auth_data["localId"]).set(tutor)
    
    
def sign_in(auth, email, password):
    """
    Seach in db email == email and password == password
    It would be not enouth, I have to set unique email in db
    """
    try:        
        auth_data = auth.sign_in_with_email_and_password(email, password)
        # print("all data:", auth_data)
        print("refreshToken:", auth_data['refreshToken']) # refreshToken
        print("idToken:", auth_data['idToken']) # idToken
    except Exception as e:
        print(e)
        return 403
    else:
        return 200  # auth_data

def get_firstname_from_id(db, id):
    return db.child("users").child(id).get().val()['firstname']

def get_all_users_data(db):
    return db.child("users").get().val()

def get_user_data_with_id(db, id):
    return db.child("users").child(id).get().val()

def user_email_already_registred(db, email):
    """
    check also in Authentication
    """
    users = db.child("users").get().each()

    if users is not None:
        for user in users:
            if user.val()['email'] == email :
                return True
    return False
        
def update_student_data_by_id(db, id, firstname, lastname, email):
    """
    from client id has to be sent in the post request automatically
    """
    try:
        data = db.child("users").child(id).get().val()

        if firstname == "":
            firstname = data['firstname']

        if lastname == "":
            lastname = data['lastname']

        if email == "":
            email = data['email']
        
        db.child("users").child(id).update(
            {
                "firstname" : firstname.title(),
                "lastname" : lastname.upper(),
                "email" : email.lower()
            }
        )

    except:
        return 400

def update_student_pedago_by_email_or_id(db, id, pedago):
    """
    from client id has to be sent in the post request automatically
    """
    try:
        data = db.child("users").child(id).get().val()
        new_details = data["details"]
        new_pedago = data["details"]["pedago"]
        for key in pedago:
            new_pedago[key] = pedago[key]

        new_details["pedago"]= new_pedago

        db.child("users").child(id).update(
            {
                "details":new_details
            }
        )

    except:
        return 404

def update_student_comptability_by_email_or_id(db, id, compta):
    """
    from client id has to be sent in the post request automatically
    """
    try:
        data = db.child("users").child(id).get().val()
        new_details = data["details"]
        new_compta = data["details"]["compta"]
        for key in compta:
            new_compta[key] = compta[key]

        new_details["compta"]= new_compta

        db.child("users").child(id).update(
            {
                "details":new_details
            }
        )

    except:
        return 404

def update_student_contract_by_email_or_id(db, id, contract):
    """
    from client id has to be sent in the post request automatically
    """
    try:
        data = db.child("users").child(id).get().val()
        new_details = data["details"]
        new_contract = data["details"]["alternant"]
        for key in contract:
            new_contract[key] = contract[key]

        new_details["alternant"] = new_contract

        db.child("users").child(id).update(
            {
                "details":new_details
            }
        )

    except:
        return 404

def update_student_info_by_email_or_id(db, id, info):
    """
    from client id has to be sent in the post request automatically
    """
    try:
        new_data = db.child("users").child(id).get().val()
        for key in info:
            if key == "firstname" or key == "lastname": # on autorise d'update que ces champs là (meme pas email)
                new_data[key] = info[key]
        

        db.child("users").child(id).update(
            {
                "details":new_data
            }
        )

    except:
        return 404

def update_teacher_data_by_id(db, id, firstname, lastname, email):
    """
    from client id has to be sent in the post request automatically
    """
    try:
        data = db.child("users").child(id).get().val()

        if firstname == "":
            firstname = data['firstname']

        if lastname == "":
            lastname = data['lastname']

        if email == "":
            email = data['email']
        
        db.child("users").child(id).update(
            {
                "firstname" : firstname.title(),
                "lastname" : lastname.upper(),
                "email" : email.lower()
            }
        )

    except:
        return 400

def update_tutor_data_by_id(db, id, firstname, lastname, email):
    """
    from client id has to be sent in the post request automatically
    """
    try:
        data = db.child("users").child(id).get().val()

        if firstname == "":
            firstname = data['firstname']

        if lastname == "":
            lastname = data['lastname']

        if email == "":
            email = data['email']
        
        db.child("users").child(id).update(
            {
                "firstname" : firstname.title(),
                "lastname" : lastname.upper(),
                "email" : email.lower()
            }
        )

    except:
        return 400

def update_staff_data_by_id(db, id, firstname, lastname, email):
    """
    from client id has to be sent in the post request automatically
    """
    try:
        data = db.child("users").child(id).get().val()

        if firstname == "":
            firstname = data['firstname']

        if lastname == "":
            lastname = data['lastname']

        if email == "":
            email = data['email']
        
        db.child("users").child(id).update(
            {
                "firstname" : firstname.title(),
                "lastname" : lastname.upper(),
                "email" : email.lower()
            }
        )

    except:
        return 400

def get_all_students_data(db):
    users = db.child("users").get()
    data={}

    for user in users.each(): 
        if user.val()['user_type'] == "student":
            data.update({user.key() : user.val()})

    return data

def get_all_teachers_data(db):
    users = db.child("users").get()
    data={}

    for user in users.each():
        if user.val()['user_type'] == "teacher":
            data.update({user.key() : user.val()})

    return data

def get_all_staffs_data(db):
    users = db.child("users").get()
    data={}
    print("route/get_all_staffs_data")
    for user in users.each():
        if user.val()['user_type'] == "staff":
            data.update({user.key() : user.val()})

    return data

def get_all_tutors_data(db):
    users = db.child("users").get()
    data={}

    for user in users.each():
        if user.val()['user_type'] == "tutor":
            data.update({user.key() : user.val()})

    return data

def get_student_pedago_by_email_or_id(db, id):
    if '@' in id:
        users = db.child("users").get()
        for user in users:
            if user.val()['email'] == id:
                if user.val()['user_type'] == "student":
                    return user.val()['details']['pedago'], 200 
        return {"message" : "id or email invalid"}, 403  
    else:
        try:
            user = db.child("users").child(id).get()
            if user.val()['user_type'] == "student":
                return user.val()['details']['pedago'], 200
        except:
            return {"message" : "id or email invalid"}, 403

def get_student_comptability_by_email_or_id(db, id):
    if '@' in id:
        users = db.child("users").get()
        for user in users:
            if user.val()['email'] == id:
                if user.val()['user_type'] == "student":
                    return user.val()['details']['compta'], 200 
        return {"message" : "id or email invalid"}, 403  
    else:
        try:
            user = db.child("users").child(id).get()
            if user.val()['user_type'] == "student":
                return user.val()['details']['compta'], 200
        except:
            return {"message" : "id or email invalid"}, 403

def get_student_contract_by_email_or_id(db, id):
    if '@' in id:
        users = db.child("users").get()
        for user in users:
            if user.val()['email'] == id:
                if user.val()['user_type'] == "student":
                    return user.val()['details']['contratPro'], 200 
        return {"message" : "id or email invalid"}, 403  
    else:
        try:
            user = db.child("users").child(id).get()
            if user.val()['user_type'] == "student":
                return user.val()['details']['contratPro'], 200
        except:
            return {"message" : "id or email invalid"}, 403

def get_student_absences_by_email_or_id(db, id):
    if '@' in id:
        users = db.child("users").get()
        for user in users:
            if user.val()['email'] == id:
                if user.val()['user_type'] == "student":
                    return user.val()['details']['nbre_absence'], 200 
        return {"message" : "id or email invalid"}, 403  
    else:
        try:
            user = db.child("users").child(id).get()
            if user.val()['user_type'] == "student":
                return user.val()['details']['nbre_absence'], 200
        except:
            return {"message" : "id or email invalid"}, 403

def get_student_pedago_credits_by_email_or_id(db, id):
    if '@' in id:
        users = db.child("users").get()
        for user in users:
            if user.val()['email'] == id:
                if user.val()['user_type'] == "student":
                    return user.val()['details']['pedago'], 200 
        return {"message" : "id or email invalid"}, 403  
    else:
        try:
            user = db.child("users").child(id).get()
            if user.val()['user_type'] == "student":
                return user.val()['details']['pedago'], 200
        except:
            return {"message" : "id or email invalid"}, 403

def delete_only_user_data_with_id(db, id):    
    db.child("users").child(id).remove()

def delete_user_with_credentials(db, auth, email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        auth.delete_user_account(user['idToken'])
        db.child("users").child(user['localId']).remove()
    except:
        print("invalid credentials")


# pagination : .order_by_child(string), .start_at(int), .end_at(int)
if __name__ == '__main__' :
    pass