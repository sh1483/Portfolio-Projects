# Make a list of various sandwiches,
#   and an empty list to hold finished sandwiches.
# Add a message that says you are out of pastrami,
#   and ensure that no pastrami sandwiches have been made with a while loop.

sandwich_orders = ['club', 'tuna', 'reuben', 'pastrami', 'peanut butter',
                   'pastrami', 'grilled cheese', 'pastrami', 'meatball']
finished_sandwiches = []

# Note that there is no pastrami, and remove from list.
print("Sorry, we are out of Pastrami!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print("\n")

# Verify each sandwich until there are no more orders.
#   Move each sandwich order into the list of finished sandwiches.
while sandwich_orders:
    current_order = sandwich_orders.pop()
    print("I have made your " + current_order.title() + " sandwich.")
    finished_sandwiches.append(current_order)

# Display all sandwiches made.
print("\nThe following sandwiches have been made:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())
