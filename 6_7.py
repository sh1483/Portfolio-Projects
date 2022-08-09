people = []

person = {
    'first_name' : 'Kristen',
    'last_name' : 'Starzynski',
    'age' : '37',
    'city' : 'Pflugerville',
    }

people.append(person)

person = {
    'first_name' : 'James',
    'last_name' : 'Haynes',
    'age' : '.75',
    'city' : 'Pflugerville',
    }

people.append(person)

person = {
    'first_name' : 'Marnie',
    'last_name' : 'Starzynski',
    'age' : '7',
    'city' : 'Pflugerville',
    }    

people.append(person)

for person in people:
    name = person['first_name'].title() + " " + person['last_name'].title()
    age = (person['age'])
    city = person['city'].title()

    print(name + ", of " + city + ", is " + age + " years old.")

