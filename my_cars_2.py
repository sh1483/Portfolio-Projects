# Importing an entire Module and accessing with dot notation.
import car_6

my_beetle = car_6.Car('volkswagen', 'beetle', 1969)
print(my_beetle.get_descriptive_name())

my_tesla = car_6.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
