def get_services_stats(db):
    """
    evenening / noon
    """
    # hack = db.child("bookingRecords").child(
    #     "12-06-2021").child("evening").child(
    #         "-Mc-i1tmgxiynH6aWk0J").child("subOrders").child(
    #             "f0460604-4bb2-40e9-8ff5-f4d3c15d60e4").child(
    #                 "products").child("0").get()

    # return hack.val()['amount'], hack.val()['name'], hack.val()['type'], hack.val()['price']
    services_stats = {}

    booking_records = db.child("bookingRecords").get()

    # return booking_records.val()

    for booking_record in booking_records.each(): # date
  
        for services in booking_record.each(): # evening / noon
            # return services.val()
            for service in services: # service id
                # return service
                pass
                # suborder
                # id
                # product
                # article

def get_noon_service_stats(db):
    """
    noon
    """
    noon_service_stats = {}
    
        
def get_evening_service_stats(db):
    """
    evenening
    """
    evening_service_stats = {}

def get_foods_stats(db):
    """
    evenening / noon !=> hot/cold drink
    """
    foods_stats = {}

def get_drink_stats(db):
    """
    evenening / noon => hot/cold drink
    """
    drinks_stats = {}