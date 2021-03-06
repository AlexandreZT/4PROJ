class User:
    def __init__(self, firstname, lastname, email, user_type=None):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.user_type = user_type

    def change_firstname(self, firstname):
        self.firstname = firstname

    def get_firstname(self):
        return self.firstname

    def get_user_type(self):
        return self.user_type

class Student(User):
    def __init__(self,
        firstname, 
        lastname,
        email,
        campus=None,
        date_of_birth=None,
        year_of_birth=None,
        street_address=None,
        gender=None,
        region=None,
        level=None,
        speciality=None,
        contratPro=None,
        previous_level=None,
        nbre_absence=None,
        age_of_entry=None,
        is_hired=None,
        lenght_month_hired=None,
        company_hired=None,
        entreprise_alternance=None,
        entreprise_alternance_address=None,
        poste_occupe=None,
        secteur_entreprise=None,
        date_debut_alternance=None,
        entry_level=None,
        year_of_entry=None,
        year_of_exit=None,
        study_lenght=None,
        level_of_exit=None,
        still_student=None,	
        compta_payment_type=None,
        compta_paid=None,
        compta_payment_due=None,	
        compta_relance=None,
        pedago=None
    ):
        super().__init__(firstname, lastname, email, user_type='student')
        # details
        self.details = {
            "campus": campus,
            "date_of_birth": date_of_birth,
            "year_of_birth" : year_of_birth,
            "street_address" : street_address,
            "gender" : gender,
            "region" : region,
            "level" : level,
            "speciality" : speciality,
            "contratPro" : contratPro,
            "previous_level" : previous_level,
            "nbre_absence" : nbre_absence,
            "age_of_entry" : age_of_entry,
            "alternant" : {
                "is_hired" : is_hired,
                "lenght_month_hired": lenght_month_hired,
                "company_hired"	: company_hired,
                "entreprise_alternance"	: entreprise_alternance,
                "entreprise_alternance_address"	: entreprise_alternance_address,
                "poste_occupe"	: poste_occupe,
                "secteur_entreprise" : secteur_entreprise,
                "date_debut_alternance": date_debut_alternance
            }, 
            "compta" : {
                "entry_level": entry_level,
                "year_of_entry"	: year_of_entry,
                "year_of_exit"	: year_of_exit,
                "study_lenght"	: study_lenght,
                "level_of_exit"	: level_of_exit,
                "still_student"	: still_student,	
                "compta_payment_type": compta_payment_type,	
                "compta_paid"	: compta_paid,
                "compta_payment_due": compta_payment_due,	
                "compta_relance": compta_relance
            },
            "pedago": pedago
        }

class Staff(User):
    def __init__(self,
        firstname, 
        lastname,
        email,
        campus=None,
        phone=None,
        role_name=None
    ):
        super().__init__(firstname, lastname, email, user_type='staff')
        self.details = {
            "campus": campus,
            "phone": phone,
            "role_name": role_name
        }
    
    def working_location(self):
        return self.details["campus"]


class Teacher(User):
    def __init__(self,
        firstname, 
        lastname,
        email,
        modules=None,
        is_available=None,
        section=None,

    ):
        super().__init__(firstname, lastname, email, user_type='teacher')
        self.details = {
            "modules": modules,
            "is_available": is_available,
            "section": section
        }
    
    def teaching_location(self):
        return self.details["section"]

class Tutor(User):
    def __init__(self,
        firstname, 
        lastname,
        email,
        phone=None,
        enterprise_name=None,
        enterprise_location=None,
        gender=None,
        job=None,
        date_of_birth=None,
        student_apprentices=[]
    ):
        super().__init__(firstname, lastname, email, user_type='tutor')
        self.details = {
            "phone": phone,
            "enterprise_name": enterprise_name,
            "enterprise_location": enterprise_location,
            "gender" : gender,
            "job" : job,
            "date_of_birth" : date_of_birth,
            "student_apprentices" : student_apprentices
        }
    
    def tutor_phone_number(self):
        return self.details["phone"]