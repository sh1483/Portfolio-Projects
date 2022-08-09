# Using Positional Arguments in a function. Order matters when typing,
# the argument.
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# Now calling it with a Keyword Argument, which defines what to look for so,
# order does not matter in the argument.
describe_pet(animal_type='cat', pet_name='socks')
describe_pet(pet_name='winky', animal_type='lizard')

