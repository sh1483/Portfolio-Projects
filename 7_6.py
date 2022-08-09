#Use 7_5.py with a conditional test to stop the loop. Use an active variable to
#control how long the loop runs. and use a break statement to exit the loop when
#a user enters a 'quit' value.

#This does not work as intended, probably should be 3 seperate files with 3
#seperate conditional tests.
prompt = "\nPlease enter your age: "
prompt += "\nEnter 'done' to finish."

active = True
while active:

    message = ""
    while message != 'done':
        message = input(prompt)

        if message != 'done':
            print(message)

while True:
    age = input(prompt)
    age = int(age)

    if message == 'done':
        break

    elif age < 3:
        print(" Admission is free!")
    elif age < 13:
        print(" The price of admission is $10.")
    else:
        print(" Admission is $15.")