# Make a list of various sandwiches,
#   and an empty list to hold finished sandwiches.

sandwich_orders = ['club', 'tuna', 'reuben', 'pastrami']
finished_sandwiches = []

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
