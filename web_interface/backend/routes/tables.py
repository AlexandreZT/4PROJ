from pyasn1.type.univ import Null
from . import stocks

def get_tables(db):
    """
    By defualt, we init 10 tables with 4 as capacity 
    Display table list, if there is less than x tables, create them
    """
    quantity = stocks.get_quantity_by_product_name(db, "tables")
    current_number_of_tables = db.child("tables").get().val()
    if (quantity == "Object not found or does not exist"):
        stocks.create_object(db=db, name="tables", quantity=10)

    if (current_number_of_tables == None):
        current_number_of_tables = 0
    else:        
        current_number_of_tables = len(current_number_of_tables)

    while current_number_of_tables < int(quantity):
        db.child("tables").push(
            {
                "tableNumber" : current_number_of_tables+1,
                "capacity" : "4",       
                "state" : "available"
            }
        )        
        current_number_of_tables+=1        
    
    return db.child("tables").get().val()

def update_table_capacity_by_id(db, id, capacity):
    tables = db.child("tables").get()
    for table in tables.each():
        if table.key() == id:            
            db.child("tables").child(id).update(
                {
                    "capacity" : capacity,
                }
            )
            return 200
    return 404
