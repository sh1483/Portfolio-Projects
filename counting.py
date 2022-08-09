#Counting and returning the number as long as it meets the parameter
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

#Using CONTINUE in a loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

#Avoiding inifinite loops
x = 1
while x <= 5:
    print(x)
    x += 1 #This line keeps the code from running endlessly
