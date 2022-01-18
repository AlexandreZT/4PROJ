from . import stocks

def create_menu_item(db, name, description, price, type):
    """
    Used when adding product from the web interface
    """
    product_types = ["side", "pizza ", "burger", "salad", "ice cream", "cake", "cold drink", "hot drink"]

    if type in product_types:
        status = stocks.create_object(db, name)

        if status == "Object already exist":
            return status
        else:
            db.child("menu").push(
                {
                    "name" : name,
                    "description" : description,
                    "price" : price, 
                    "type" : type
                }
            )
            return "Product successfully added"
        
def get_menu_data(db):
    return db.child("menu").get().val()

def get_menu_item_data_with_id(db, id):
    return db.child("menu").child(id).get().val()

def get_all_drinks_data(db):
    menu = db.child("menu").get()
    drink_types = ["cold drink", 'hot drink']
    drinks={}

    for item in menu.each():
        if item.val()['type'] in drink_types:
            drinks.update({item.key() : item.val()})

    return drinks

def get_all_foods_data(db):
    menu = db.child("menu").get()
    food_types = ["side", "pizza", "burger", "salad", "ice cream", "cake"]
    foods={}

    for item in menu.each():
        if item.val()['type'] in food_types :
            foods.update({item.key() : item.val()})

    return foods

def delete_menu_item_with_id(db, id):
    name = get_menu_item_data_with_id(db, id)['name']
    stocks.delete_object(db, name)
    db.child("menu").child(id).remove()  

def update_menu_item_data_with_id(db, id, name, description, price, type):
    """
    If new name is already taken in stocks table, I can't do the operation
    """
    product_types = ["side", "pizza ", "burger", "salad", "ice cream", "cake", "cold drink", "hot drink"]

    taken_name = False

    if name != "":
        taken_name = stocks.check_if_object_is_already_taken(db, name)

    print("name_taken:", not taken_name)

    if (not taken_name):
        try:
            data = db.child("menu").child(id).get().val()

            previous_name = get_menu_item_data_with_id(db, id)['name']

            if name == "":
                name = data['name']

            if description == "":
                description = data['description']

            if price == "":
                price = data['price']

            if type == "":
                type = data['type']

            if type in product_types:
                db.child("menu").child(id).update(
                    {
                        "name" : name,
                        "description" : description,
                        "price" : price,
                        "type" : type,
                    }
                )
            else:
                print("This role does not exist")
        except:
            print("expect")
            return 404 # wrong
    else:
        return 404 # name already taken
    
    print(previous_name)

    if (previous_name != name):
        stocks.update_name_by_old_product_name(db, previous_name, name)
    else:
        print("All rights !")


# + : .order_by_child(string), .start_at(int), .end_at(int)