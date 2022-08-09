# Make shirts Large by default with a message that says 'I love Python',
# Make a large shirt and a medium shirt with the default message, and a shirt of,
# Any size with a different message.
def make_shirt(shirt_text, shirt_size='Large'):
    """Display information about a shirt"""
    print(f"\nYour shirt size is: {shirt_size.title()}.")
    print(f"Your {shirt_size.title()} shirt says: {shirt_text.title()}.")


make_shirt('I love Python')

make_shirt('I love Python', shirt_size='Medium')

make_shirt(shirt_text='Pineapple', shirt_size='Small')
