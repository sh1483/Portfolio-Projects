#creating a Dictionary
cities = {
    'la paz' : {
    'population' : '766,468',
    'country' : 'bolivia',
    'fact' : 'highest administrative capital in the world',
    },
    'berlin' : {
    'population' : '3,769,495',
    'country' : 'germany',
    'fact' : 'first documented in the 13th century',
    },
    'shanghai' : {
    'population' : '24,280,000',
    'country' : 'china',
    'fact' : "world's busiest container port",
    },
    'brisbane' : {
    'population' : '2,500,000',
    'country' : 'australia',
    'fact' : 'one of the oldest cities in Australia',
    },
    'lome' : {
    'population' : '837,437',
    'country' : 'togo',
    'fact' : 'the temperature stays generally in the 80s year round',
    },
    'new brunswick' : {
    'population' : '55,676',
    'country' : 'united states',
    'fact' : 'the home of Rutgers University',
    },
}

#for every city, plus their info in cities
for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    fact = city_info['fact'].title()

#printing out each line of information
    print("\n" + city.title() + " is in " + country + ".")
    print("\tIt has a population of about " + str(population) + ".")
    print("\tNoted for:\n\t\t" + fact)