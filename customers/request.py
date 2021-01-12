CUSTOMERS = [
    {
      "email": "art@art.com",
      "password": "art",
      "name": "art art",
      "id": 1
    },
    {
      "email": "dart@art.com",
      "password": "dart",
      "name": "dart fart",
      "id": 2
    },
    {
      "email": "part@art.com",
      "password": "part",
      "name": "part part",
      "id": 3
    },
    {
      "email": "smil@s.org",
      "password": "yup",
      "name": "Tilly Smilly",
      "id": 4
    },
    {
      "email": "bigsandyland@hotmail.com",
      "password": "b",
      "name": "b  b",
      "id": 5
    }
  ]

def get_all_customers():
    return CUSTOMERS
    
def get_single_customer(id):
    request_customer = None

    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer

def create_customer(customer):
    max_id =CUSTOMERS[-1]["id"]

    new_id = max_id + 1

    customer["id"] = new_id

    CUSTOMERS.append(customer)

    return customer        