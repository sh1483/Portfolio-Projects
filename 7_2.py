
#Seating a table as long as there are not more than 8 people
diners = input("How many are in your party? ")
diners = int(diners)

if diners <= 8:
    print("\tRight this way.")
else:
    print("\tYour table will be ready shortly.")
