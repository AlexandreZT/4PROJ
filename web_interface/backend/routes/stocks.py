from pyasn1.type.univ import Null


def create_object(db, name, quantity=0):
    """
    You can track drinks and foods quantities
    Also tables are a type of object
    By default, when creating an object there is 0 quantity
    The name must be unique, it is used as identifier
    """
    stocks = db.child("stocks").get().val()
    
    for object in stocks:
        if stocks[object]["name"] == name.lower():
            return "Object already exist"

    db.child("stocks").push({
        "name" : name.lower(),
        "quantity" : quantity
    })

def update_quantity_by_product_name(db, name, quantity):
    stocks = db.child("stocks").get()
    for object in stocks.each():
        if object.val()['name'] == name:
            db.child("stocks").child(object.key()).update(
                {
                    "quantity" : quantity
                }
            )
            if object.val()['name'] == "tables":
                stocks_data = db.child("tables").get()
                current_number_of_tables = db.child("tables").get().val()
                if current_number_of_tables == None:
                    current_number_of_tables = 0
                else:        
                    current_number_of_tables = len(current_number_of_tables)
                for object in stocks_data.each()[::-1]:  
                    if current_number_of_tables != quantity:      
                        db.child("tables").child(object.key()).remove()
                        current_number_of_tables-=1
            return 200 # 'Quantity updated'
    return 404 # 'Object not found or does not exist'


def update_name_by_old_product_name(db, old_product_name, new_name):
    if (old_product_name == "tables" or new_name=="tables"):
        return "This name is reserve !"

    stocks = db.child("stocks").get()
    for object in stocks.each():
        if object.val()['name'] == old_product_name:
            db.child("stocks").child(object.key()).update(
                {
                    "name" : new_name
                }
            )
            return 'Name updated'
    return 'Object not found or does not exist'  


def get_quantity_by_product_name(db, name):
    """
    When customers want to place an order, we can check the availability of the wanted product.
    """
    stocks = db.child("stocks").get()
    for object in stocks.each():
        if object.val()["name"] == name:
            return object.val()["quantity"]
    return 'Object not found or does not exist'


def get_stocks(db):
    return db.child("stocks").get().val()


def check_if_object_is_already_taken(db, name):
    stocks = db.child("stocks").get() # get_stocks(db)
    print("name:", name)
    for object in stocks.each():
        print(object.val()["name"])
        if object.val()["name"] == name:
            return True    
    return False


def delete_object(db, name):
    stocks = db.child("stocks").get()
    for object in stocks.each():
        if object.val()['name'] == name:
            db.child("stocks").child(object.key()).remove()
            return "Object deleted"
    return "Object not found or does not exist"


def consumme_product(db, name, quantity):
    """
    While  clients consume, stocks decrease
    ex : 1 coca = -1 coca in stock    
    """
    availability = get_quantity_by_product_name(db, name)

    if (availability == "Object not found or does not exist"):
        return availability

    elif (int(availability) < quantity):
        return name+": "+str(quantity-int(availability))+" missing" # They must reOrder

    else: # => int(availability) >= quantity
        update_quantity_by_product_name(db, name, int(availability)-quantity)
        return "We bring you "+ str(quantity) +" "+name     