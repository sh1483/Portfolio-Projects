# Use 8_10.py to call a send function send_messages() with a copy of the list,
# Messages. After calling the function, print both lists to show the original,
# List has retained its message.
def show_messages(messages):
    """Print all messages in the list."""
    print("Showing all messages:")
    for message in messages:
        print(message.title())


def send_messages(messages, sent_messages):
    """Print each message, and then move it to sent_messages."""
    print("\nSending all messages:")
    while messages:
        current_message = messages.pop()
        print(current_message.title())
        sent_messages.append(current_message)


messages = ['hannah likes peas', 'ty ate yogurt', 'margot is fat']
show_messages(messages)

sent_messages = []
send_messages(messages[:], sent_messages)

print("\nFinal lists:")
print(messages)
print(sent_messages)
