
# sort permanently changes list order to alphabetical 
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

cars.sort()
print("\nHere is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

cars = ['bmw','audi','toyota','subaru']

print("\nLet's reverse the list of cars.")
print(cars)
cars.reverse()
print(cars)

#printing specific words in different cases
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')



