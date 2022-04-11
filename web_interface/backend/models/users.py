class User:
    def __init__(self, firstname, lastname, email, user_type=None):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.user_type = user_type

    def change_firstname(self, firstname):
        self.firstname = firstname

    def get_firstname(self):
        print(f"Hey {self.firstname}")

    def get_user_type(self):
        print(f"You're {self.user_type}")

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
        compta_relance=None
    ):
        super().__init__(firstname, lastname, email, user_type='Student')
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
            }
        }
                

student = Student(
    firstname="Alexandre",
    lastname="zitouni tinlot",
    email="alexandre.zitounitinlot@supinfo.com",
    # optionnal :

    # details
    date_of_birth="02/10/1979",
    year_of_birth="1979",
    street_address="40 Nova Crossing",
    gender="male",
    region="str",
    level="M.ENG 1",
    speciality="Intelligence Artificielle",
    contratPro="true",
    previous_level="Bac",
    nbre_absence=4,
    age_of_entry=22,

    # alternant
    is_hired=True,
    lenght_month_hired=3,
    company_hired="Wavestone",
    entreprise_alternance="Adobe",
    entreprise_alternance_address="3 Holy Cross Avenue",
    poste_occupe="Software Engineer",
    secteur_entreprise="Software",
    date_debut_alternance="2021-11-11 13:14:55 UTC",

    # compta
    entry_level="B.ENG 1",
    year_of_entry=2001,
    year_of_exit=2003,
    study_lenght=2,
    level_of_exit="B.ENG 2",
    still_student=False,	
    compta_payment_type="Comptant/OPCA/Echelonnement",	
    compta_paid=True,
    compta_payment_due=0,	
    compta_relance=False

)

# student.get_firstname()
# student.get_user_type()
# student.change_firstname("Guillaume")
# print(student.__dict__)

# print(student.details)

# print(student.details["alternant"])

# print(student.details["compta"])

# dict
# class MyClass(object):
#     @classmethod
#     def fromdict(cls, d):
#         allowed = ('key1', 'key2')
#         df = {k : v for k, v in d.items() if k in allowed}
#         return cls(**df)

#     def __init__(self, key1, key2):
#         self.key1 = key1
#         self.key2 = key2

# dict = {'key1': 'value1', 'key2': 'value2', 'redundant_key': 'redundant_value'}

# ob = MyClass.fromdict(dict)

# print(ob.key1)
# print(ob.key2)
# print(ob.__dict__)

# +++
# class Bunch(object):    
#     def __init__(self, test="PLS", **fields): 
#         self.__dict__ = fields
#         self.test = test
        
        
# p = Bunch(test = "yes", x=2.3, y=4.5)
# print (p)               

# print (p.__dict__)