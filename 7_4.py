#Loop that prompts a user to enter pizza toppings until they enter 'quit',
#Printing a message that says you are adding that topping.
prompt = "Please enter a topping for your pizza:"
prompt += "\nEnter 'quit' when you are finished."

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"Adding {topping.title()}!")
        