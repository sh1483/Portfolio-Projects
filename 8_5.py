# Make describe_city that accepts a city and country it is in. Have it print a,
# Simple sentence. Give parameter for the country by default. Call a city not,
# In the default country.
def describe_city(city_name, country_name='Germany'):
    """Display a city in a country"""
    print(f"\n{city_name.title()} is in {country_name.title()}.")


describe_city('Berlin')

describe_city('Munich')

describe_city('Oslo', country_name='Norway')
