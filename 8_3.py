# Write a function called make_shirt() that accepts the size and the text,
# Of a message that should be printed on the shirt. Call once using positional,
# arguments and once using keyword arguments.
def make_shirt(shirt_size, shirt_text):
    """Display information about a shirt"""
    print(f"\nYour shirt size is: {shirt_size.title()}.")
    print(f"Your {shirt_size.title()} shirt says: {shirt_text.title()}.")


make_shirt('large', "I like tacos!")

# Now calling it with a Keyword Argument, which defines what to look for so,
# order does not matter in the argument.
make_shirt(shirt_size='medium', shirt_text='Fun for all!')
