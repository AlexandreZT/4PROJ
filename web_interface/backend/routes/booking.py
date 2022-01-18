from math import ceil

from pyasn1.type.univ import Null

def save_booking(db, nb_persons=6, id_user="test_id", arrival_time="21-05-31-14:00"):
    """
    """
    departure_time = arrival_time[0:9]+str(int(arrival_time.split('-')[3].split(':')[0])+1)+':00' # todo : there is a new format

    nb_tables_needed = ceil(nb_persons / 4) # todo : 4 is table capacity, the value must be dynamique

    tables = db.child("table").get()

    available_tables = 0
    available_tables_id = []

    for table in tables.each():        
        if table.val()['available'] == True:
            available_tables_id.append(table.key())
            available_tables+=1
    
    if (available_tables != 0):
        if (available_tables >= nb_tables_needed):            
            for i in range(0, nb_tables_needed):
                db.child("table").child(available_tables_id[i]).update({      
                    "available" : False
                })   

                db.child("booking").push({
                    "userId" : id_user,
                    "arrivalTime" : arrival_time,
                    "departureTime" : departure_time,
                    "nbPersons" : nb_persons,
                    "tableIds" : available_tables_id                    
                })
            return "Two tables are now reserved"
        else:
            return "Not enough tables"
    else:
        return "We are full"