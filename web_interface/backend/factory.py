from models.users import Student, Teacher, Staff, Tutor
from routes import users


"""
This file only explain how to manage user object (models)
To CRUD an user in DB, user requests from routes, just call right route as listed in main.py & routes/users.py
"""

# exemple création d'un étudiant
student = Student(
    firstname="Alexandre",
    lastname="Student",
    email="alexandre.zitounitinlot@supinfo.com",
    # optionnal :

    # details
    date_of_birth="02/10/1979",
    year_of_birth="1979",
    street_address="40 Nova Crossing",
    gender="male",
    region="Ile-de-France",
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

"""
Student data access
"""
student.get_firstname()
# student.get_user_type()
# student.change_firstname("Guillaume")
# print(student.__dict__)

# print(student.details)

# print(student.details["alternant"])

# print(student.details["compta"])



# exemple création membre d'un intervenant

teacher = Teacher(
    firstname="AAA",
    lastname="Teacher",
    email="aaa.teacher@supinfo.com",
    # optionnal :
    campus="Lyon"
    
)
teaching_location = teacher.teaching_location()
print(teaching_location)
# exemple création membre d'un staff
# 903;Vitoria;Plomer;vitoriaplomer@supinfo.com;Caen;Full Professor

staff = Staff(
    firstname="AAA",
    lastname="Staff",
    email="aaa.bobo@supinfo.com",
    # optionnal :
    campus="Lyon"
    
)
working_location = staff.working_location()
print(working_location)

"""
traces
"""

tutor = Tutor(
    firstname="AAA",
    lastname="Staff",
    email="aaa.bobo@supinfo.com",
    phone="0102030405",
    enterprise_name='google'
    enterprise_location='Paris'
)

phone_number = tutor.tutor_phone_number()
print(phone_number)
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

