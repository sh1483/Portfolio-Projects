# Poll users about their dream vacation and print results of poll.

responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Where would you go for a dream vacation? ")

# Store the response in a dictionary.
    responses[name] = response

# Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond?" + " (yes/no) ")
    if repeat == 'no':
       polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name.title() + " would like to vacation in " + response.title() + ".")
