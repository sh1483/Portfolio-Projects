# Make a list containing a few short messages. Pass the list to a function,
# called show_messages(), which prints each message.
# Use Ctrl+F/R or Ctrl+Shift+F/R to change all instances of something. (find and replace)

# Passing a list
def show_messages(messages):
    """Print messages from a list."""
    for message in messages:
        msg = message.title()
        print(msg)


messages = ['hannah likes peas', 'ty ate yogurt', 'margot is fat']
show_messages(messages)
