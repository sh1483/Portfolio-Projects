# Write a function that stores information about a car in a dictionary. The function,
# Should always receive a manufacturer and model name. It should then accept an,
# Arbitrary number of keyword arguments. Call the function with the required,
# Information and two other name-value pairs, such as a color or an optional,
# Feature. Your function should work for a call like this one:
# car = vehicle('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that's returned to make sure all the information,
# Was stored correctly.
def vehicle(make, model, **options):
    """Build a dictionary about cars."""
    car_dict = {
        'make': make.title(),
        'model': model.title(),
        }
    for option, value in options.items():
        car_dict[option] = value

    return car_dict


car_profile = vehicle('subaru', 'forester',
                  color='black',
                  trim='sport')
bob_car = vehicle('chrysler', 'le baron', color='tan', style='convertible')
print(bob_car)

james_car = vehicle('chevrolet', '1500', color='green', motor='v8')
print(james_car)

my_old_accord = vehicle('honda', 'accord', year=1991, color='white',
        headlights='popup')
print(my_old_accord)

my_outback = vehicle('subaru', 'outback', color='blue', tow_package=True)
print(my_outback)
