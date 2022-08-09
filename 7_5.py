#Enter an age and receive back the price of a ticket based on that age.
prompt = "\nPlease enter your age: "
prompt += "\nEnter 'quit' when you are finished."

while True:
    age = input(prompt)
    if age == 'quit':
       break
    age = int(age)

    if age < 3:
        print(" Admission is free!")
    elif age < 13:
        print(" The price of admission is $10.")
    else:
        print(" Admission is $15.")
