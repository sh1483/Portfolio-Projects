# Using Default Values in a function.
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')

# The simplest way to use this is to call just the dogs name.
describe_pet('willie')

# To describe a pet that isn't a dog, you can do this:
describe_pet(pet_name='harry', animal_type='hamster')
