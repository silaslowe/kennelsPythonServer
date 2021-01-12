LOCATIONS = [
    {
        "id": 1,
        "name": "North",
    },
    {
        "id": 2,
        "name": "South",
        "species": "Dog",
    },
    {
        "id": 3,
        "name": "Central",
        "species": "Cat",
    }
]


def get_all_locations():
    return LOCATIONS

def get_single_location(id):
    requested_location = None

    for location in LOCATIONS:
        if location["id"] == id:
            requested_location = location

    return requested_location        