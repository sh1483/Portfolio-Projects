
favorite_places = {
    'john' : ['cancun', 'topeka'], 
    'mary' : ['toledo', 'fargo'],
    'thomas' : ['venice', 'berlin', 'oslo']
    }

for name, places in favorite_places.items():
    print("\n" + name.title() + " likes the following places:")
    for place in places:
        print("- " + place.title())


