# Write a function called city_country that takes the name of a city and its country,
# It should return a string formatted like this: "Santiago, Chile". Call the,
# Function with at least 3 city-country pairs and print the values.
def city_country(city, country):
    """Return a string like "Santiago, Chile'."""
    return f"{city.title()}, {country.title()}"


city = city_country('santiago', 'chile')
print(city)

city = city_country('dresden', 'germany')
print(city)

city = city_country('cape town', 'south africa')
print(city)
