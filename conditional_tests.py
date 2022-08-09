
car = 'Subaru'
print(car)
print(car == 'audi')
print(car != 'audi')
print(car == 'bmw')
print(car == 'porshe')
print(car != 'ferrari')
print(car != 'mercedes')
print(car == 'mercedes')
print(car != 'lamborghini')
print(car == 'lamborghini')
print(car == 'bmw')
print(car == 'subaru')
print(car == 'Subaru')
print(car.lower() == 'subaru')#means case doesn't matter

print("\n")

if car != 'Audi':
    print(f"The car is not an Audi")

print("\n")

#these don't seem to be working how I want. Wrong returns.
cars = ['Audi','bmw','mercedes','porshe','lotus']
print(car == 'ford')
print(car in cars != 'chevrolet')#should be True
print(car in cars == 'Audi')#should be True
print(car in cars == 'Audi' or 'ford')#returns ford for some reason
print(car in cars == 'Audi' or car in cars == 'ford')#returns false, not true
print(car in cars == 'Audi' and 'ford')
print(car != 'chevrolet')

#not the fix for the above
if car in cars == "audi" or 'ford':
    print("\nTrue")
elif car in cars != "audi" or 'ford':
    print("\nFalse")

#still not the fix for the above
cars = ['Audi','bmw','mercedes','porshe','lotus']
for car in cars:
    print(car == 'ford')
    print(car in cars != 'chevrolet')#should be True
    print(car in cars == 'Audi')#should be True
    print(car in cars == 'Audi' or 'ford')#returns ford for some reason
    print(car in cars == 'Audi' or car in cars == 'ford')#returns false, not true
    print(car in cars == 'Audi' and 'ford')
    print(car != 'chevrolet')

age_0 = 21
age_1 = 15
print(age_0 == 15)
print(age_0 != 22)
print(age_0 == 21 and age_1 != 15)
print(age_0 == 21 or age_1 != 15)
print(age_0 == 22 or age_1 != 15)

#Steges of Life exercise 5-6
age = 52
if age < 2:
    print("\nYou are a baby.")
elif age < 4:
    print("\nYou are a toddler.")
elif age < 13:
    print("\nYou are a kid")
elif age < 20:
    print("\nYou are a teenager.")
elif age <65:
    print("\nYou are an adult.")
else:
    print("\nYou are an elder.")

age = 52
if age < 2:
    stage = 'baby'
elif age < 4:
    stage = 'toddler'
elif age < 13:
    stage = 'kid'
elif age < 20:
    stage = 'teenager'
elif age <65:
    stage = 'adult'
else:
    stage = 'elder'
print(f"\nYou are an {stage}.")

#Favorite Fruit exercise 5-7
favorite_fruits = ['kiwi','guava','raspberries']

for favorite_fruits in favorite_fruits:
    if favorite_fruits == "pineapple":
        print(True)
    else:
        print(f"\nYou really like {favorite_fruits}!")

'pineapple' in favorite_fruits

if favorite_fruits == 'pineapple':
    print(f"1")
else:
    print(f"2")

#SOLUTIONS FOR FAVORITE_FRUITS EXERCISE (FROMT FIRST EDITION OF BOOK)
favorite_fruits = ['blueberries', 'salmonberries', 'peaches']

if 'bananas' in favorite_fruits:
    print("You really like bananas!")
if 'apples' in favorite_fruits:
    print("You really like apples!")
if 'blueberries' in favorite_fruits:
    print("You really like blueberries!")
if 'kiwis' in favorite_fruits:
    print("You really like kiwis!")
if 'peaches' in favorite_fruits:
    print("You really like peaches!")