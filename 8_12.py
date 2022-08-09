# Write a function that accepts a list of items a person wants on a sandwich.
# The function should have one parameter that collects as many items as the function,
# Call provides, and should print a summary of the sandwich being ordered.
# Call the function 3 times, using a different number of arguments each time.
def make_sandwich(*toppings):
    """Print a list of sandwich toppings."""
    print("\nMaking a sandwich with:")
    for topping in toppings:
        print(f"- {topping}")


make_sandwich('salami', 'capicola', 'prosciutto', 'parmesan', 'olive oil')
make_sandwich('peanut butter', 'grape jelly')
make_sandwich('lettuce', 'tomato', 'bacon', 'mayonnaise')
